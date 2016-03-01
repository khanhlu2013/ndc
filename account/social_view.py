import json

from django.http import HttpResponse
from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import authenticate,login

from ndc_user.models import Ndc_user
from account import get_social_profile,email_after_signup

def _get_social_account_name(client_id):
    if client_id == settings.OAUTH_GOOGLE_ID:
        return 'google'

def _login(social_account_name,auth_code,redirect_uri,request):
    user = authenticate(social_account_name=social_account_name, auth_code=auth_code, redirect_uri=redirect_uri)
    if user is not None:
        if user.is_active:
            login(request, user)
            response = {'token':{}}
            return HttpResponse(json.dumps(response),content_type="application/json")                                  
        else:
            response = {'token':{'error_message':'Your account is un-active'}}
            return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        response = {'token':{'error_message':'Social account is not registered. Login failed.'}}
        return HttpResponse(json.dumps(response),content_type="application/json")

def _signup(social_account_name,auth_code,redirect_uri,ndc_user_param):
    profile = get_social_profile.exe(social_account_name=social_account_name, auth_code=auth_code, redirect_uri=redirect_uri)
    error_message = None
    try:
        Ndc_user.objects.create_user(
            email = profile['email'],
            first_name = profile['first_name'],
            last_name = profile['last_name'],
            phone = ndc_user_param.get('phone',None),
            gender = ndc_user_param['gender'] if ndc_user_param.get('gender',None) else None,
            is_email_verify = True,
            password = None
        )
        email_after_signup.social(social_account_name,ndc_user_param,profile)
    except IntegrityError as e:
        error_message = profile['email'] + ' account is existed. Please login instead.'

    response = {'token':{'error_message':error_message}}
    return HttpResponse(json.dumps(response),content_type="application/json")    

def auth(request):
    """
        handle both signup and login
            . signup -> param must contain a ndc_user 
            . login -> param don't contain a ndc_user
    """
    social_account_name = _get_social_account_name(request.POST['clientId'])
    auth_code = request.POST['code']
    redirect_uri = request.POST['redirectUri']
    ndc_user_param = json.loads(request.POST['ndc_user']) if request.POST.get('ndc_user',None) else None
    if ndc_user_param == None:
        return _login(
            social_account_name=social_account_name,
            auth_code=auth_code,
            redirect_uri=redirect_uri,
            request=request
        )
    else:
        return _signup(
            social_account_name=social_account_name,
            auth_code=auth_code,
            redirect_uri=redirect_uri,
            ndc_user_param=ndc_user_param
        )
import json
import uuid

from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate,login

from ndc_user.models import Ndc_user
from account import email_after_signup

def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            if user.is_email_verify:
                login(request, user)
                response = {}
                return HttpResponse(json.dumps(response),content_type="application/json")
            else:
                response = {'error_message':'Please activate your account by checking your email.'}
                return HttpResponse(json.dumps(response),content_type="application/json")                
        else:
            response = {'error_message':'Your account is un-active'}
            return HttpResponse(json.dumps(response),content_type="application/json")
    else:
        response = {'error_message':'Login failed'}
        return HttpResponse(json.dumps(response),content_type="application/json")


def signup_view(request):
    """
        expect ndc_user in the post request data
        return response dictionary, if there is an error, this dic will contain error_message
    """
    ndc_user_param = json.loads(request.POST['ndc_user'])
    error_message = None
    try:
        user = Ndc_user.objects.create_user(
            email = ndc_user_param['email'],
            first_name = ndc_user_param['first_name'],
            last_name = ndc_user_param['last_name'],
            phone = ndc_user_param.get('phone',None),
            gender = ndc_user_param['gender'] if ndc_user_param.get('gender',None) else None,
            is_email_verify = False,
            password = ndc_user_param.get('password',None)
        )
        email_activation_key = str(uuid.uuid4())
        user.email_activation_key = email_activation_key
        user.save()

        email_after_signup.non_social(
            ndc_user_param=ndc_user_param,
            email_activation_key=email_activation_key,
            redirect_server_url=request.build_absolute_uri('/')
        )      
    except IntegrityError as e:
        error_message = ndc_user_param['email'] + ' account is existed. Please login instead.'

    response = {'error_message':error_message}
    return HttpResponse(json.dumps(response),content_type="application/json")
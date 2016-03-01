from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
import json
import requests
from ndc_user.models import Ndc_user
from django.contrib.auth import authenticate,login

def exe(social_account_name,auth_code,redirect_uri):
    if social_account_name == 'google':
        return _get_google_profile(auth_code,redirect_uri)

def _get_google_profile(auth_code,redirect_uri):
    token_url = 'https://accounts.google.com/o/oauth2/token'
    profile_url = 'https://www.googleapis.com/userinfo/v2/me'

    payload = dict(client_id=settings.OAUTH_GOOGLE_ID,
                    redirect_uri=redirect_uri,
                    client_secret=settings.OAUTH_GOOGLE_SECRETE,
                    code=auth_code,
                    grant_type='authorization_code')

    # Step 1. Exchange authorization code for access token.
    r = requests.post(token_url, data=payload)
    token = json.loads(r.text)
    headers = {'Authorization': 'Bearer {0}'.format(token['access_token'])}

    # Step 2. Retrieve information about the current user.
    r = requests.get(profile_url, headers=headers)
    profile = json.loads(r.text)
    return {
        'email' : profile['email'],
        'first_name' : profile['given_name'],
        'last_name' : profile['family_name']
    }
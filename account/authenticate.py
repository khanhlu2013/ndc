from ndc_user.models import Ndc_user
from account import get_social_profile

class Social_account_authenticate(object):
    def authenticate(self, social_account_name=None, auth_code=None, redirect_uri=None):
        profile = get_social_profile.exe(social_account_name=social_account_name, auth_code=auth_code, redirect_uri=redirect_uri)
        ndc_user = None
        try:
            ndc_user = Ndc_user.objects.get(email=profile['email'])
            if ndc_user.has_usable_password():
                return None
            else:
                return ndc_user            
        except Ndc_user.DoesNotExist:
            return None


    def get_user(self, user_id):
        try:
            return Ndc_user.objects.get(pk=user_id)
        except Ndc_user.DoesNotExist:
            return None    
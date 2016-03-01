from ndc_user.models import Ndc_user

def get_lst():
    return Ndc_user.objects.all()
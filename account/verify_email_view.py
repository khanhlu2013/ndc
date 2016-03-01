from ndc_user.models import Ndc_user
from django.http import HttpResponse

def exe(request,email_activation_key):
    user = Ndc_user.objects.get(email_activation_key=email_activation_key)
    
    if user.is_email_verify == False:
        user.is_email_verify = True
        user.save()

    html = "<html><body><h3>your email: %s is verified. Thank you.</h3></body></html>" % user.email
    return HttpResponse(html)

from django.core.mail import send_mail
from membership.models import Membership

def _get_membership_type_name_base_on_id(membership_type_id):
    membership_type = None
    for item in Membership.MEMBERSHIP_TYPE_LST:
        if membership_type_id == item[0]:
            membership_type = item[1]
            break
    return membership_type

def social(social_account_name,ndc_user_param,profile):
    membership_type_id=ndc_user_param['membership_type'] if ndc_user_param.get('membership_type',None) else None
    membership_type_name = _get_membership_type_name_base_on_id(membership_type_id) if membership_type_id != None else None

    message = 'You have signup for a NDC account using your ' + social_account_name + ' account.\n'
    if membership_type_name:
        message += 'You have request to be a ' + membership_type_name + ' NDC member.\n'
    else:
        message += 'You have not signup to be a NDC member. If you decide to change your mind, you can contact us or change membership setting in the NDC app.\n'
    
    message += 'You can login NDC app using your ' + social_account_name + ' account.\n'

    send_mail(
        subject='Welcome to NDC, ' + profile['first_name'] + ' ' + profile['last_name'], 
        message=message,
        from_email=None,
        recipient_list=[profile['email']],
        fail_silently=False
    )

def non_social(ndc_user_param,email_activation_key,redirect_server_url):
    membership_type_id = ndc_user_param['membership_type'] if ndc_user_param.get('membership_type',None) else None
    membership_type_name = _get_membership_type_name_base_on_id(membership_type_id) if membership_type_id != None else None
    user_name = ndc_user_param['first_name'] + ' ' + ndc_user_param['last_name']
    message = '<p>You have signup for a NDC account.</p>'
    if membership_type_name:
        message += '<p>You have request to be a ' + membership_type_name + ' NDC member.</p>'
    else:
        message += '<p>You have not signup to be a NDC member.</p>'

    if ndc_user_param.get('password',None):
        message += '<p>You can login to NDC app with your email and password that you registered with us.</p>'
    else:
        message += '<p>You have not signup to use NDC app.</p>'
    
    # http://127.0.0.1:8000
    message += ('<a href="%s/auth/email_verification/%s/">click here to verify your email.</a>' % (redirect_server_url,email_activation_key,))
    print(message)
    send_mail(
        subject='Welcome to NDC, ' + user_name, 
        message=None,
        from_email=None,
        recipient_list=[ndc_user_param['email']],
        fail_silently=False,
        html_message=message
    )
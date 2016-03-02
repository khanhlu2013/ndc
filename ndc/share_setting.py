from membership.models import Membership
from ndc_user.models import Ndc_user
from event.models import Event_rate,Attendance
from django.conf import settings
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from ndc_user.serialize import Ndc_user_serializer

def set(context,login_user):
    share_setting = {};
    
    share_setting['MEMBERSHIP_TYPE_LST'] = [ {'internal':data[0],'external':data[1]} for data in Membership.MEMBERSHIP_TYPE_LST]
    share_setting['GENDER_LST'] = [ {'internal':data[0],'external':data[1]} for data in Ndc_user.GENDER_LST]
    share_setting['DANCE_RATE_LST'] = [ {'internal':data[0],'external':data[1]} for data in Event_rate.DANCE_RATE_LST]
    share_setting['PAYMENT_TYPE_LST'] = [ {'internal':data[0],'external':data[1]} for data in Attendance.PAYMENT_TYPE_LST]
    share_setting['PHONE_REGX'] = settings.PHONE_REGX
    share_setting['WHY'] = settings.WHY
    
    if login_user.is_anonymous():
        share_setting['LOGIN_USER'] = None
    else:
        share_setting['LOGIN_USER'] = Ndc_user_serializer(login_user).data

    context['SHARE_SETTING_JSON_STRING'] = json.dumps(share_setting,cls=DjangoJSONEncoder)
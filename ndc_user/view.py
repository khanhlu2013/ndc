from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import PermissionDenied
from ndc_user import dao
from ndc_user.serialize import Ndc_user_serializer
from django.http import HttpResponse
import json

def get_lst_view(request):
    if not request.user.has_perm('ndc_user.change_ndc_user'):
        raise PermissionDenied
    lst = dao.get_lst()
    lst_serialized = Ndc_user_serializer(lst,many=True).data
    return HttpResponse(json.dumps(lst_serialized, cls=DjangoJSONEncoder),content_type='application/json')

def get_login_user_view(request):
    if request.user.is_anonymous():
        serialized = None
    else:
        serialized = Ndc_user_serializer(request.user,many=False).data
    return HttpResponse(json.dumps(serialized, cls=DjangoJSONEncoder),content_type='application/json')
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
import json
from membership.models import Membership,MembershipOverlapError
from ndc_user.models import Ndc_user
from membership.serialize import Membership_serializer
from datetime import datetime
from django.db import IntegrityError

def _iso_date_str_to_python_date(iso_date_str):
    fmt="%Y-%m-%dT%H:%M:%S.%fZ"
    return datetime.strptime(iso_date_str, fmt)


def edit_view(request):
    if not request.user.has_perm('membership.change_membership'):
        raise PermissionDenied

    membership_json = json.loads(request.POST['membership'])
    date_time = _iso_date_str_to_python_date(membership_json['start_date'])
    date_only = date_time.date()
    membership = Membership.objects.get(pk=membership_json['id'])
    membership.start_date = date_only
    membership.membership_type = membership_json['membership_type']
    membership.is_issue_key = membership_json['is_issue_key']

    response = {}
    try:
        membership.save()
        membership_serialized = Membership_serializer(membership).data
        response['membership'] = membership_serialized
    except MembershipOverlapError:
        response['error'] = 'Membership overlap error'
    
    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder),content_type='application/json')


def add_view(request):
    if not request.user.has_perm('membership.add_membership'):
        raise PermissionDenied
    data = json.loads(request.POST['clump_data'])

    account_id = data['account_id']
    membership_type = data['membership_type']
    is_issue_key = data['is_issue_key']
    start_date = _iso_date_str_to_python_date(data['start_date']).date()
    ndc_old_id = data['ndc_old_id']

    membership = Membership(
        start_date=start_date,
        membership_type=membership_type,
        is_issue_key=is_issue_key,
        user_id=account_id
    )
    response = {}
    try:
        membership.save()
        membership_serialized = Membership_serializer(membership).data

        if ndc_old_id!=None:
            user = Ndc_user.objects.get(pk=account_id)
            user.ndc_old_id = ndc_old_id
            user.save()

        response['membership'] = membership_serialized
    except MembershipOverlapError:
        response['error'] = 'Membership overlap error'
    except IntegrityError:
        response['error'] = 'Integrity error - id might already in used'

    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder),content_type='application/json')

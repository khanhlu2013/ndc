from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from event import dao
from event.serialize import Event_serializer,Attendance_serializer,Default_rate_serializer,Venue_serializer
from django.http import HttpResponse
import json
import datetime

def create_event_view(request):
    if not request.user.has_perm('event.add_event'): 
        raise PermissionDenied

    data = json.loads(request.POST['clumped_data'])
    venue_id = data['venue_id']
    start_time = datetime.datetime.strptime(data['start_time'], '%Y-%m-%dT%H:%M:%S.%fZ').time()
    duration = data['duration']
    date_only = datetime.datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
    weekly = data['weekly']
    lst_serialized = None
    error = None

    try:
        event_lst = dao.create_event(venue_id,date_only,start_time,duration,weekly)    
        lst_serialized = Event_serializer(event_lst,many=True).data
    except IntegrityError as e:
        print(e)
        error = 'Possible duplicate date and venue when create events'
    
    return HttpResponse(json.dumps({'event_lst':lst_serialized,'error':error}, cls=DjangoJSONEncoder),content_type='application/json')

def insert_or_edit_event_default_rate_view(request):
    if not request.user.has_perm('event.change_default_rate') or not request.user.has_perm('event.add_default_rate'): 
        raise PermissionDenied

    data = json.loads(request.POST['clumped_data'])
    default_rate = dao.insert_or_edit_event_default_rate(data['rate'],data['amount'])
    serialized = Default_rate_serializer(default_rate,many=False).data
    return HttpResponse(json.dumps(serialized, cls=DjangoJSONEncoder),content_type='application/json')

def get_venue_lst_view(request):
    lst = dao.get_venue_lst()
    lst_serialized = Venue_serializer(lst,many=True).data
    return HttpResponse(json.dumps(lst_serialized, cls=DjangoJSONEncoder),content_type='application/json')

def get_default_event_rate_lst_view(request):
    if not request.user.has_perm('event.change_default_rate') or not request.user.has_perm('event.add_default_rate'): 
        raise PermissionDenied

    lst = dao.get_event_default_rate_lst()
    serialized = Default_rate_serializer(lst,many=True).data
    return HttpResponse(json.dumps(serialized,cls=DjangoJSONEncoder),content_type='application/json')

def get_event_view(request):
    if not request.user.has_perm('event.add_event') or not request.user.has_perm('event.change_event'):
        raise PermissionDenied

    event_id = request.GET['event_id']
    event = dao.get_event(event_id)
    serialized = Event_serializer(event,many=False).data
    return HttpResponse(json.dumps(serialized, cls=DjangoJSONEncoder),content_type='application/json')

def get_live_event_view(request):
    if not request.user.has_perm('event.event_checkin'):
        raise PermissionDenied

    event_id = request.GET['event_id']
    event = dao.get_live_event(event_id)
    serialized = None
    if event != None:
        serialized = Event_serializer(event,many=False).data
    return HttpResponse(json.dumps(serialized, cls=DjangoJSONEncoder),content_type='application/json')

def get_live_event_lst_view(request):
    if not request.user.has_perm('event.event_checkin'):
        raise PermissionDenied

    lst = dao.get_live_event_lst()
    lst_serialized = Event_serializer(lst,many=True).data
    return HttpResponse(json.dumps(lst_serialized, cls=DjangoJSONEncoder),content_type='application/json')

def get_event_lst_view(request):
    if not request.user.has_perm('event.add_event') or not request.user.has_perm('event.change_event'):
        raise PermissionDenied

    lst = dao.get_event_lst()
    lst_serialized = Event_serializer(lst,many=True).data
    return HttpResponse(json.dumps(lst_serialized, cls=DjangoJSONEncoder),content_type='application/json')

def insert_attendance_view(request):
    if not request.user.has_perm('event.event_checkin'):
        raise PermissionDenied
        
    data = json.loads(request.POST['clumped_data'])
    attendance = dao.insert_attendance(
        event_id = data['event_id'],
        user_id = data.get('user_id',None),
        anonymous_first_name = data.get('anonymous_first_name',None),
        anonymous_last_name = data.get('anonymous_last_name',None),
        event_rate_id = data['event_rate_id'],
        payment_type = data.get('payment_type',None)
    )

    serialized = Attendance_serializer(attendance,many=False).data
    return HttpResponse(json.dumps(serialized, cls=DjangoJSONEncoder),content_type='application/json')
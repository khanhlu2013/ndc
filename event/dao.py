from event.models import Event,Event_rate
from ndc_user.models import Ndc_user
from django.conf import settings
import datetime
from event.models import Event_rate,Attendance,Default_rate,Venue
from django.db import DataError

def get_venue(venue_id):
    return Venue.objects.get(pk=venue_id)

def _get_default_rate_from_lst_based_on_rate_type(lookup_rate_type,default_rate_lst):
    for default_rate in default_rate_lst:
        if default_rate.rate == lookup_rate_type:
            return default_rate

def create_event(venue_id,date,start_time,duration,weekly):
    event_lst = []
    default_rate_lst = get_event_default_rate_lst()
    for i in range(weekly):
        event = Event.objects.create(
            date = date + datetime.timedelta(days=i*7),
            start_time = start_time,
            duration = duration,
            venue_id = venue_id
        )
        for default_rate in [item for item in default_rate_lst if item.amount != None]:
            event_rate = Event_rate.objects.create(
                event = event,
                rate = default_rate.rate,
                amount = default_rate.amount
            )

        event_lst.append(event)
    return event_lst

def get_event_lst():
    return Event.objects.all()

def get_venue_lst():
    return Venue.objects.all()

def get_event_default_rate_lst():
    """
        We hardcode a list of default rate for events. if we have not defined a certain hardcoded default rate for the system,
        instead of NOT return that rate, we DO return that rate with null amount. I think this implementation simplify the client 
        side implementation for managing default rate.
    """
    result_lst = []
    default_rate_lst = Default_rate.objects.all()
    for rate_type in [item[0] for item in Event_rate.DANCE_RATE_LST]:
        defined_default_rate = _get_default_rate_from_lst_based_on_rate_type(rate_type,default_rate_lst)
        if defined_default_rate == None:
            defined_default_rate = Default_rate(rate=rate_type,amount=None)
        result_lst.append(defined_default_rate)
    return result_lst
    
def insert_or_edit_event_default_rate(rate,amount):
    obj,created = Default_rate.objects.update_or_create(defaults={'amount':amount},rate=rate)
    return obj

def get_event(event_id):
    return Event.objects.get(pk=event_id)

def get_live_event(event_id):
    e = Event.objects.get(pk=event_id)
    if e.is_live():
        return e
    else:
        return None

def get_live_event_lst():
    now = datetime.datetime.now()
    min_range = now - datetime.timedelta(hours=48)#not a most optimized algorithm but the most optimize algorithm involved raw sql. 48 came from max(start_time) + max(duration)
    query = Event.objects.filter(date__range=(min_range, now))
    un_verified_lst = list(query)
    result = [event for event in un_verified_lst if event.is_live()]
    return result

def insert_attendance(event_id,user_id,anonymous_first_name,anonymous_last_name,event_rate_id,payment_type):
    event_rate = Event_rate.objects.get(pk=event_rate_id)
    if event_rate.event.id != event_id:
        raise DataError

    return Attendance.objects.create(
        event_id = event_id,
        user_id = user_id,
        anonymous_first_name = anonymous_first_name,
        anonymous_last_name = anonymous_last_name,
        event_rate_id = event_rate_id,
        payment_type = payment_type
    )
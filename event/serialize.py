from rest_framework import serializers,fields
from event.models import Event,Venue,Attendance,Event_rate,Default_rate
from membership.serialize import Membership_serializer
from django.contrib.auth.models import Group
from ndc_user.serialize import Ndc_user_serializer

class Venue_serializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name','start_time','duration')
        
class Event_non_recursive_serializer(serializers.ModelSerializer):
    venue = Venue_serializer(many=False)

    class Meta:
        model = Event
        fields = (
            'id',
            'date',
            'start_time',
            'duration',
            'venue'
        )

class Event_rate_serializer(serializers.ModelSerializer):
    event = Event_non_recursive_serializer(many=False)
    class Meta:
        model = Event_rate
        fields = ('id','rate','amount','event')

class Attendance_serializer(serializers.ModelSerializer):
    event = Event_non_recursive_serializer(many=False)
    user = Ndc_user_serializer(many=False)
    event_rate = Event_rate_serializer(many=False)

    class Meta:
        model = Attendance
        fields = ('id','date_time','user','anonymous_first_name','anonymous_last_name','event_rate','payment_type','event')

class Default_rate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Default_rate
        fields = ('id','rate','amount')

class Event_serializer(serializers.ModelSerializer):
    venue = Venue_serializer(many=False)
    attendance_set = Attendance_serializer(many=True)
    event_rate_lst = Event_rate_serializer(many=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'date',
            'start_time',
            'duration',
            'venue',
            'attendance_set',
            'event_rate_lst'
        )


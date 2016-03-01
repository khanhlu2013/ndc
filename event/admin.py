from django.contrib import admin
from .models import Event,Venue,Event_rate,Attendance,Default_rate

admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Event_rate)
admin.site.register(Attendance)
admin.site.register(Default_rate)
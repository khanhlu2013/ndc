from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from event import view

urlpatterns = patterns('',
    url(r'^get_live_event_lst$',login_required(view.get_live_event_lst_view)),  
    url(r'^get_event_lst$',login_required(view.get_event_lst_view)),      
    url(r'^get_live_event$',login_required(view.get_live_event_view)), 
    url(r'^get_event$',login_required(view.get_event_view)),      
    url(r'^insert_attendance$',login_required(view.insert_attendance_view)),  
    url(r'^get_event_default_rate_lst$',login_required(view.get_default_event_rate_lst_view)),      
    url(r'^get_venue_lst$',login_required(view.get_venue_lst_view)),          
    url(r'^insert_or_edit_event_defaut_rate$',login_required(view.insert_or_edit_event_default_rate_view)),     
    url(r'^create_event$',login_required(view.create_event_view)),     
)      
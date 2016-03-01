from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from ndc_user import view

urlpatterns = patterns('',
    url(r'^get_lst$',login_required(view.get_lst_view)),  
    url(r'^get_login_user$',view.get_login_user_view),  
)      
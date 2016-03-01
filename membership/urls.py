from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from membership import view

urlpatterns = patterns('',
    url(r'^add$',login_required(view.add_view)),  
    url(r'^edit$',login_required(view.edit_view)),  
)      
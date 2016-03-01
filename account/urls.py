from django.conf.urls import patterns,url
from account import social_view,non_social_view,verify_email_view

urlpatterns = patterns('',
    url(r'^social_auth$',social_view.auth),  
    url(r'^non_social_signup$',non_social_view.signup_view),      
    url(r'^non_social_login$',non_social_view.login_view),          
    url(r'^email_verification/([-0-9a-z]{36})/$',verify_email_view.exe),      
)
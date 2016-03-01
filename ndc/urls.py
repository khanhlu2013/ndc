from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from ndc import view
import account.urls
import ndc_user.urls
import membership.urls
import event.urls

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ndc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',view.anonymous_app_view.as_view(),name=settings.LOGIN_URL),   
    url(r'^django_admin/', include(admin.site.urls)),
    url(r'^manage/$',login_required(view.manage_app_view.as_view()),name=settings.NDC_APP_URL),  
    url(r'^account/logout/$','django.contrib.auth.views.logout_then_login',name=settings.LOGOUT_URL),    
    url(r'^auth/', include(account.urls)),   
    url(r'^ndc_user/', include(ndc_user.urls)),   
    url(r'^event/', include(event.urls)),   
    url(r'^membership/', include(membership.urls)),
)
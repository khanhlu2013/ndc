from django.views.generic import TemplateView
from django.conf import settings
from ndc import share_setting
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator


class manage_app_view(TemplateView):
    # if settings.IS_USE_CDN:
    #     template_name = 'dist/deploy/manage_app.html'
    # else:
    #     template_name = 'dist/develop/manage_app.html'

    template_name = 'manage_app.html'
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(manage_app_view, self).dispatch(*args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(manage_app_view,self).get_context_data(**kwargs)
        share_setting.set(context,self.request.user)
        return context          

class login_view(TemplateView):
    template_name = 'login.html'
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(login_view, self).dispatch(*args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(login_view,self).get_context_data(**kwargs)
        share_setting.set(context,self.request.user)
        return context             
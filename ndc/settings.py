from unipath import Path
import os
import sys

PROJECT_ROOT = Path(__file__).ancestor(2)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'ndc_user',
    'membership',
    'event',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request', 
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter':'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'filters': [],   
            'propagate': True,
            'level':'INFO',
        }, 
    },
}

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
WSGI_APPLICATION = 'ndc.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


SITE_ID = 3
ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------

DEBUG = os.environ.get('DEBUG') == '1'
TEMPLATE_DEBUG = DEBUG
IS_USE_CDN = os.environ.get('IS_USE_CDN') == '1' #we only use Content Deliver Network CDN when deploy. for local developmet we are not.
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_URL = os.environ.get('STATIC_URL')
TEMPLATE_DIRS = ( PROJECT_ROOT.child('templates'), )
ROOT_URLCONF = 'ndc.urls'
LOGIN_URL = 'login_named_url'
LOGOUT_URL = 'logout_named_url'
MANAGE_APP_URL = 'manage_app_named_url'
LOGIN_REDIRECT_URL = MANAGE_APP_URL
OAUTH_GOOGLE_ID = os.environ.get('OAUTH_GOOGLE_ID')
OAUTH_GOOGLE_SECRETE = os.environ.get('OAUTH_GOOGLE_SECRETE')

#- this will read the environment variable DATABASE_URL and translate it for django to understand
import dj_database_url
DATABASES = {'default': dj_database_url.config()}

#- STATICFILES_DIRS and STATICFILES_FINDERS are ONLY need for LOCAL development because Django will host these static file on its local server for us. In deployment, we will host this static file our self using amazon s3, and access it though the static_url setting
# STATICFILES_DIRS = ( PROJECT_ROOT.child('static'), )
STATICFILES_DIRS = ( 
    PROJECT_ROOT.child('static').child('build'), 
    PROJECT_ROOT.child('static').child('collected_js_lib'), 
)
STATICFILES_FINDERS = ( 'django.contrib.staticfiles.finders.FileSystemFinder', )
STATIC_ROOT = PROJECT_ROOT.child('static_root')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
"""
    membership type is hardcoded because there is only 4 type: platinum, gold, silver,brone. On the server side i only need
    to reserve an integer id to represent the type. on the client side, an integer id to represent type is not user friendly
    so we need an object to represent membership type which pretty much translate the id into a more human friendly object 
    that contain a name for the type and more info if we need to expand this object such as is_public, cost ... (if we want to)
    I save this harcode info on the server then passing it down to all the client webpage.
"""
AUTH_USER_MODEL = 'ndc_user.Ndc_user'
AUTHENTICATION_BACKENDS = (
    "account.authenticate.Social_account_authenticate",
    "django.contrib.auth.backends.ModelBackend"
)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'khanhlu2013@gmail.com'
DEFAULT_FROM_EMAIL = 'khanhlu2013@gmail.com'
EMAIL_HOST_PASSWORD = '_Mother3169_'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PHONE_REGX = '^([0-9]{3})-([0-9]{3})-([0-9]{4})$'
WHY = {
    'NDC_ACCOUNT' : 
    [
        "Why do you need an NDC account?",
        "You need a NDC account to be a NDC member, or use NDC app, or both. For non-member, you can use your NDC account to signin at the front desk of your NDC dance event. This way, we know how much you spend at NDC and if you spend more than a certain membership cost, we can give that membership benefit to you."
    ],
    'SOCIAL_ACCOUNT' : 
    [
        "Why use your social account to sign up for a NDC account?",
        "You can use your facebook or google account to sign up for a NDC account. This way, you do not have to verify your email with us. You login to your NDC app with your social account (no need to create and remember another password.)"
    ],                
    'VERIFY_EMAIL' : 
    [
        "Why do i need to verify your email?",
        "When you signup using your social account, your email for that social account is verified with that party. When signup by using your email, we do not know if it is valid. After signup, please check your email and click on the email verification link to complete the signup process."
    ],
    'NDC_APP_PASSWORD' : 
    [
        "Why do i need to create a password?",
        "To access NDC app, we need to know who you are by login with your email and password. If you do not like to create and remember a password to access NDC app, you can use your social account to signup instead."
    ],
    'NDC_MEMBER' : 
    [
        "Why do you want to be a NDC member?",
        "You save $ if you are a frequent dancer. You can have a key to the club to practice dancing."
    ],
    'NDC_APP' : 
    [
        "Why use NDC app?",
        "Non-member can use ndc app to upload picture, video, DJ playlist for events. Member use app to reserve practice sessions with our google calendar."
    ]
}
"""
    CUSTOM PERMISSION THAT NEED TO SETUP IN DATABASE
        . (model,code_name,name) = (event,event_checkin, can checkin live event)

    GUIDELINE PERMISSION FOR GROUP
        . admin = [
                        event.default_rate.add_default_rate,
                        event.default_rate.change_default_rate, 
                        event.event.add_event 
                        event.event.change_event        
                        event.event.event_checkin,                         
                        ndc_user.ndc_user.add_user, 
                        ndc_user.ndc_user.change_user, 
                ]
        . staff = [
                        event.event.event_checkin
                ]
"""
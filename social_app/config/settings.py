"""
Django settings for social_app project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(#9w7^erht)_9ztnt3dk!cm5@xlz_+g9&u(20d5qx&to%i=88)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',
    'faceb_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_KEY')

''' Here is the bug display FACEBOOK_SCOP = ['useremail'] '''
# SOCIAL_AUTH_FACEBOOK_SCOPE = os.environ.get('FACEBOOK_SCOPE')

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = os.environ.get('FACEBOOK_PROFILE_EXTRA_PARAMS')
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = os.environ.get('FACEBOOK_EXTRA_DATA')



LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# from django.conf import settings

# if getattr(settings, 'FACEBOOK_APP_AUTH', False):
#     from social.backends.facebook import \
#             FacebookAppOAuth2 as FacebookBackendBase
# else:
#     from social.backends.facebook import FacebookOAuth2 as FacebookBackendBase


# REDIRECT_HTML = """
# <script type="text/javascript">
#     var domain = 'https://apps.facebook.com/',
#         redirectURI = domain + '{{ FACEBOOK_APP_NAMESPACE }}' + '/';
#     window.top.location = 'https://www.facebook.com/dialog/oauth/' +
#     '?client_id={{ FACEBOOK_KEY }}' +
#     '&redirect_uri=' + encodeURIComponent(redirectURI) +
#     '&scope={{ FACEBOOK_EXTENDED_PERMISSIONS }}';
# </script>
# """


# class FacebookBackend(FacebookBackendBase):
#     def auth_html(self):
#         key, secret = self.get_key_and_secret()
#         namespace = self.setting('NAMESPACE', None)
#         scope = self.get_scope()
#         if scope:
#             scope = self.SCOPE_SEPARATOR.join(scope)
#         ctx = {
#             'FACEBOOK_APP_NAMESPACE': namespace or key,
#             'FACEBOOK_KEY': key,
#             'FACEBOOK_EXTENDED_PERMISSIONS': scope,
#             'FACEBOOK_COMPLETE_URI': self.redirect_uri,
#         }
#         tpl = self.setting('LOCAL_HTML', 'facebook.html')
#         return self.strategy.render_html(tpl=tpl, html=REDIRECT_HTML,
#                                          context=ctx)
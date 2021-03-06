"""
Django settings for social_secretary project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from social_secretary import secret_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3%k^rx7jc&ryxeh^)wd5kxss(8=f&00=+gt7yzqndwiw5zs)(t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social_secretary.ss_app',
    'userena',
    'guardian',
    'easy_thumbnails',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# userena package
from userena import settings as userena_settings

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

userena_settings.USERENA_ACTIVATION_REQUIRED = False
userena_settings.USERENA_SIGNIN_AFTER_SIGNUP = True
userena_settings.USERENA_SIGNIN_REDIRECT_URL = "/accounts/%(username)s/"

AUTH_PROFILE_MODULE = 'ss_app.MyProfile'
ANONYMOUS_USER_ID = -1
#LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'


ROOT_URLCONF = 'social_secretary.urls'

WSGI_APPLICATION = 'social_secretary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'social_secretary',
        'USER': 'social_secretary',
        'PASSWORD': secret_settings.DEFAULT_DATABASE_PASSWORD,
        'HOST': 'localhost',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = '/media'

# facebook app settings
FACEBOOK_APP_ID = secret_settings.FACEBOOK_APP_ID
FACEBOOK_APP_SECRET = secret_settings.FACEBOOK_APP_SECRET

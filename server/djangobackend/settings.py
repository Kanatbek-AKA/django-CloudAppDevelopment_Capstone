"""
Django settings for djangobackend project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

import environ
environ.Env()
environ.Env().read_env(os.path.join('../../functions/.env'))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Read and write file outside the django project
BASE_ADD_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.abspath(os.path.join(BASE_ADD_FILE, '../cloudant/data/'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ao5z(o(z@cvzodm99d32jkxa5e8a1!q_4sqss5-a%n6tg$#h$+'  # os.environ.get('KEYS')

# SECURITY WARNING: don't run with debug turned on in production!
# if the repo runs on local machine set Debug to true else debug false hosted
DEBUG = True

# APPEND_SLASH = True    #
ALLOWED_HOSTS = ["127.0.0.1"]

# CORS_ORIGIN_WHITELIST
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5000',
    'http://localhost:5000',
]   


# Application definition
INSTALLED_APPS = [
    'djangoapp.apps.DjangoappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    "corsheaders",
    'guardian',
    'oauth2_provider',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_referrer_policy.middleware.ReferrerPolicyMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',

]

REFERRER_POLICY = 'no-referrer'

# SESSION_COOKIES_HTTP=True
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True
# SECURE_HSTS_SECONDS = 300  # set low, but when site is ready for deployment, set to at least 15768000 (6 months)
# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_HSTS_PRELOAD = True    # 
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SAMESITE = 'Strict'
# SESSION_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'

# LANGUAGE_COOKIE_DOMAIN = None
# CSRF_TRUSTED_ORIGINS = ['https://...host.....app']
# INTERNAL_IPS = []
# CONN_MAX_AGE = 0 # restrict
CONN_HEALTH_CHECKS = True  # improve the robustness of connection


# Need to FIX CSS/JS after enabling
# CSP_DEFAULT_SRC = ("'none'",)
# CSP_STYLE_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_FONT_SRC = ("'self'",)
# CSP_IMG_SRC = ("'self'",)


ROOT_URLCONF = 'djangobackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'djangoapp/static'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangobackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
MEDIA_URL = '/media/'
# 
# MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'api', 'uploads'))
# MEDIA_URL = '/uploads/'
# FRONTEND_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'dist', 'frontend'))

# Securing
AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend', 
    'guardian.backends.ObjectPermissionBackend'
    )

OAUTH2_PROVIDER = {
    'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups',
        'packages': 'Access to your packages',
    },
}

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
# }

# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis'

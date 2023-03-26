"""
Django settings for my_site project.

<<<<<<< HEAD
Generated by 'django-admin startproject' using Django 4.1.3.
=======
Generated by 'django-admin startproject' using Django 4.1.6.
>>>>>>> 0eb7a81 (Blog Website Up and Running)

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
<<<<<<< HEAD
=======
from os import getenv
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
>>>>>>> 0eb7a81 (Blog Website Up and Running)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'django-insecure-_z6pj799(x+fj*lphvspq8#)3f(4k71cicr@3l#!v^nlx6lr1l'
=======
SECRET_KEY = env('SECRET_KEY')
>>>>>>> 0eb7a81 (Blog Website Up and Running)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = []
=======
ALLOWED_HOSTS = [
    getenv('APP_HOST', '127.0.0.1')
]
>>>>>>> 0eb7a81 (Blog Website Up and Running)


# Application definition

INSTALLED_APPS = [
<<<<<<< HEAD
    'book_outlet',
    'blog.apps.BlogConfig',
=======
    'blog', 
>>>>>>> 0eb7a81 (Blog Website Up and Running)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'my_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
=======
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'djangoblog',
        'PASSWORD': 'Itispassword37',
        'HOST': 'django-blog.cwld8fd1gprx.eu-north-1.rds.amazonaws.com',
        'PORT': '5432',
>>>>>>> 0eb7a81 (Blog Website Up and Running)
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

<<<<<<< HEAD
STATIC_URL = 'static/'
=======
# Collect all the static files at one place to serve during production phase
# python manage.py collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
>>>>>>> 0eb7a81 (Blog Website Up and Running)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

<<<<<<< HEAD
STATICFILES_DIRS = [ 
    BASE_DIR / 'static'
]
=======

MEDIA_ROOT = BASE_DIR / 'uploads'
MEDIA_URL = '/user-media/'
>>>>>>> 0eb7a81 (Blog Website Up and Running)
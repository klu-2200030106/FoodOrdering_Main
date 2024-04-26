"""
Django settings for Restaurant_management_system project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hz8(ou+a7kq72y2@$*w1uhmo)dy_g++9lul1p*+mw%=jgw5(5f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# settings.py
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Application definition

INSTALLED_APPS = [
    'rangefilter',
    'shop.apps.ShopConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'system',
    'captcha',
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

ROOT_URLCONF = 'system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['system/templates'],
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

WSGI_APPLICATION = 'system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    #
    #     # 'ENGINE': 'django.db.backends.mysql',
    #     # 'NAME': 'OnlineFood',  # name of the database
    #     # 'USER': 'root',
    #     # 'PASSWORD': '',
    #     # 'HOST': 'localhost',
    #     # 'PORT': '3306',
    #
    #     # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     # 'NAME': 'OnlineFoodOrdering',
    #     # 'USER': 'postgres',
    #     # 'PASSWORD': 'BUNNY123',
    #     # 'HOST': 'localhost',
    #     # 'PORT': '5432',
    #
    # }
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'OnlineFood',  # database name
    'USER': 'postgres',
    'PASSWORD': 'BUNNY123',
    'HOST': 'localhost',
    'PORT': '5432',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Managing media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# SMTP Configuration

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # or your SMTP server
EMAIL_PORT = 587  # or 465 for SSL
EMAIL_USE_TLS = True  # or EMAIL_USE_SSL for SSL
EMAIL_HOST_USER = 'kandularohit143@gmail.com'
EMAIL_HOST_PASSWORD = 'Rohith@123'


# settings.py
STRIPE_PUBLISHABLE_KEY = 'pk_test_51P9kMoSJ9mQgnAH43K4msnXImPzx4N5xDLBdGrjfgPMN2n3jN9yz7I4Km8JolXvege4kJUWaVmnzabPjgN8FRsBO00uyns212T'

STRIPE_PRIVATE_KEY = 'sk_test_51P9kMoSJ9mQgnAH4yirea7ylCPWNuAespgGgWZLMZ7zVuwKkWbBodu8jhkWGdlYeJZCF5AMuYG6qJz6Vrf1mqPO100wipi3TYm'
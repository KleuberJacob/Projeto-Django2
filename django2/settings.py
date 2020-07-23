"""
Django settings for django2 project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url

# Utilizando PostgreSQL para subir para produçao no Heroku, pois nao aceita BD MySQL
DATABASES = {
    'default': dj_database_url.config()
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e-zscx4&$+c@1cer@tz@4*@hw166pkb)!%6^eeta4tsk8k55-t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'bootstrap4',
    'stdimage',
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

ROOT_URLCONF = 'django2.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'django2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Comentando a DATABASES, toda nossa aplicaçao foi desenvolvida utilizando como banco de dados o MySQL, porém para que
# possamos coloca-la em produçao utilizando a plataforma (gratuita do Heroku) teremos de utilizar o banco de dados
# PostgreSQL, pois o Heroku nao da suporte de forma gratuita ao MySQL.
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django2',
        'USER': 'geek',
        'PASSWORD': 'university',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
"""
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configurando sistema de envio de emails de teste dentro do próprio Django
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configurando sistema de envio de emails caso possua um servidor de e-mail no servidor de produçao.
"""
EMAIL_HOST = 'localhost'      <== Normalmente é utilizada essa nomenclatura
EMAIL_HOST_USER = 'no-reply@seudominio.com.br'        <== Domínio responsável pelo envio do email
EMAIL_PORT = 587   <== Normalmente utilizada porta 587, mas pode ser outra
EMAIL_USER_TLS = True  <== Padrao de segurança 
EMAIL_HOST_PASSWORD = 'senha do email'  
"""

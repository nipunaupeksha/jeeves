"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'td(x+qt=tpa#462420nd_p63h0^r1^=92rbrxdusu5@a0+jb)d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.html'

# Application definition

INSTALLED_APPS = [
    'conf.apps.ConfConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'timelog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'timelog.middleware.TimeLogMiddleware',
    'logging_middleware.ConfLoggingMiddleware',
]

ROOT_URLCONF = 'cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # insert your TEMPLATE_DIRS here
        ],
#        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django_jinja.loaders.AppLoader',
                'django_jinja.loaders.FileSystemLoader',
                # insert your TEMPLATE_LOADERS here
            ],
            'debug' : True
        },
    },
]
    
WSGI_APPLICATION = 'cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    '/var/www/static/',
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"


# PROJECT SPECIFIC
# possible phases are submit, review, final
CONF_PHASE = 'submit'

LOG_PATH = os.path.join(BASE_DIR, '..', 'logs/')
TIMELOG_LOG = os.path.join(LOG_PATH, 'timelog.log')
SQL_LOG = os.path.join(LOG_PATH, 'sqllog.log')

LOGGING = {
  'version': 1,
  'formatters': {
    'plain': {
      'format': '%(asctime)s %(message)s'},
    },
  'handlers': {
    'timelog': {
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': TIMELOG_LOG,
      'maxBytes': 1024 * 1024 * 5,  # 5 MB
      'backupCount': 5,
      'formatter': 'plain',
    },
    'sqllog': {
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': SQL_LOG,
      'maxBytes': 1024 * 1024 * 5,  # 5 MB
      'backupCount': 5,
      'formatter': 'plain',
    },
  },
  'loggers': {
    'timelog.middleware': {
      'handlers': ['timelog'],
      'level': 'DEBUG',
      'propogate': False,
     },
    'timing_logging': {
      'handlers': ['timelog'],
      'level': 'DEBUG',
      'propogate': False,
     },
    'logging_middleware': {
      'handlers': ['sqllog'],
      'level': 'DEBUG',
      'propogate': False
    },
  },
}


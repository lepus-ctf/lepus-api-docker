# encoding=utf-8
from lepus.settings import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

PUSH_EVENT_URL = "http://push:8001/events/"
STATIC_ROOT = "/app/static"

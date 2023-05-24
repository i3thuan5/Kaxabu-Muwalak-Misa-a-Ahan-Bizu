import os
from pathlib import Path
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from django.core.exceptions import ImproperlyConfigured

from .settings import *  # noqa

SECRET_KEY = os.getenv('SECRET_KEY')

VIRTUAL_HOST = os.getenv('VIRTUAL_HOST').split(',')

ALLOWED_HOSTS = VIRTUAL_HOST

CSRF_TRUSTED_ORIGINS = []
for host in VIRTUAL_HOST:
    CSRF_TRUSTED_ORIGINS.append(
        'https://{}'.format(host)
    )


DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
LANGUAGE_COOKIE_SECURE = True

CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SAMESITE = 'Strict'

CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

if os.getenv('SSL_REDIRECT', default=True) and VIRTUAL_HOST != ['localhost']:
    # Tsi̍t-pîng要求HTTPS，因為localhost開發時袂按呢做，所以開發時關--起-來。
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    SECURE_HSTS_SECONDS = 10
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'ithuan',
        'HOST': 'postgres',
        'PORT': '',
    },
}

AWS_S3_USE_SSL = True
AWS_S3_SIGNATURE_VERSION = 's3v4'


SENTRY_DSN = os.getenv('SENTRY_DSN', default=None)

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=0.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )

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
    'kukautian': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root',
        'PASSWORD': 'ithuan',
        'HOST': 'mariadb',
        'PORT': '',
    }
}

STATIC_ROOT = '/staticfiles/'

MEDIA_URL = '/media/'
MEDIA_ROOT = Path('/app/media')

CELERY_TASK_ALWAYS_EAGER = False
CELERY_BROKER_URL = 'amqp://khautso:bitbe@rabbitmq:5672/ithuan'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')

EMAIL_USE_TLS = (
    os.getenv('EMAIL_USE_TLS', default='').lower() == 'true')
EMAIL_USE_SSL = (
    os.getenv('EMAIL_USE_SSL', default='').lower() == 'true')

if EMAIL_USE_TLS and EMAIL_USE_SSL:
    raise ImproperlyConfigured(
        "EMAIL_USE_TLS, EMAIL_USE_SSL bē-sái tâng-tsê True")
elif EMAIL_USE_TLS:
    EMAIL_PORT = 587
elif EMAIL_USE_SSL:
    EMAIL_PORT = 465
else:
    EMAIL_PORT = 25

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_RECEIPIENT_LIST = [
    'carolchou@mail.moe.gov.tw',
    'ithuan@ithuan.tw',
]
ADMINS = [('ithuan', 'ithuan+kautian@ithuan.tw'), ]

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

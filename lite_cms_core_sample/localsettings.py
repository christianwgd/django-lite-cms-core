# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
import os

import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "fb14=awt0cyou3mg!ocpty-+7gq0nkhz^2&wkhzbbl=uja=u#*"

# Allowed development hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1"]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'wgdnet.db'),
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "wgdnet",
        "USER": "postgres",
        "PASSWORD": "mistral",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mail')
DEFAULT_FROM_EMAIL = 'info@wgdnet.de'

# Friendly captcha
# FRC_WIDGET_MODULE_JS = 'https://unpkg.com/friendly-challenge@0.9.5/widget.module.min.js'
# FRC_WIDGET_JS = 'https://unpkg.com/friendly-challenge@0.9.5/widget.min.js'
FRC_CAPTCHA_SECRET = 'A1K36DIF4JCQDNTAC8F8AR511N6R4JACM8SAM07349GN4T6S7IPKVV9A6M'
# FRC_CAPTCHA_SECRET = ''
FRC_CAPTCHA_SITE_KEY = 'FCMLR69V35DCGCDK'
# FRC_CAPTCHA_SITE_KEY = ''
# FRC_CAPTCHA_VERIFICATION_URL = 'https://api.friendlycaptcha.com/api/v1/siteverify'
# FRC_CAPTCHA_VERIFICATION_URL = 'https://eu-api.friendlycaptcha.eu/api/v1/puzzle'
FRC_CAPTCHA_VERIFICATION_URL = 'https://global.frcapi.com/api/v2/captcha/siteverify'
FRC_CAPTCHA_FAIL_SILENT = False

CONTACT_USE_HONEYPOT = True
CONTACT_USE_ANTISPAM = True

ANTISPAM_USE_REMOTE_SERVICE = True
ANTSPAM_USER_AGENT = "test-client"
ANTISPAM_API_KEY = "invalid_api_key"
ANTISPAM_API_URL = "http://localhost:8000/"

# Process metrics
PROCESS_METRICS_TOKEN = 'w0t5dp7f_ee25^pfyg*h-sp@jq(sd^tw^bn-s9o2$eun985^l5'

# def get_country_from_ip(ip):
#     return requests.get(f"https://ipapi.co/{ip}/country_name/").text


# REQUEST_LOG_COUNTRY_FUNC = get_country_from_ip


# Logging
logfile = os.path.join(BASE_DIR, 'log/wgdnet.log')
spooflog = os.path.join(BASE_DIR, 'log/spoof.log')
captchalog = os.path.join(BASE_DIR, 'log/captcha.log')
# LOGGING = {
#     'version': 1,
#
#     'root': {
#         'level': 'INFO',
#         'handlers': ['default'],
#     },
#
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(name)s %(funcName)s %(message)s'
#         },
#     },
#
#     'handlers': {
#         'default': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': logfile,
#             'maxBytes': 1024*1024*5,  # 5 MB
#             'backupCount': 5,   # 5 Generationen aufheben
#         },
#         'spoof_logfile': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': spooflog,
#             'maxBytes': 1024*1024,  # 1 MB
#             'backupCount': 5,   # 5 Generationen aufheben
#         },
#         'friendly_captcha': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': captchalog,
#             'maxBytes': 1024*1024,  # 1 MB
#             'backupCount': 5,   # 5 Generationen aufheben
#         },
#     },
#
#     'loggers': {
#         'django.db.backends': {
#             'level': 'CRITICAL',
#         },
#         'django.security.DisallowedHost': {
#             'handlers': ['spoof_logfile'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.friendly_captcha': {
#             'handlers': ['friendly_captcha'],
#             'level': 'INFO',
#             'propagate': False,
#         }
#     }
# }
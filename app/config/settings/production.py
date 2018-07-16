import sys

from .base import *


secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))


# RUNSERVER = len(sys.argv) > 1 and sys.argv[1] == 'runserver'
RUNSERVER = 'runserver' in sys.argv
DEBUG = False

if RUNSERVER:
    DEBUG = True
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
    ]


WSGI_APPLICATION = 'config.wsgi.production.application'

DATABASES = secrets['DATABASES']
DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

# Log
# LOG_DIR 존재하면 그냥 쓴다
LOG_DIR = '/var/log/django'

# 존재하지 않는다면
# if not os.path.exists(LOG_DIR):
#     # ROOT_DIR/.log를 쓴다
#     LOG_DIR = os.path.join(ROOT_DIR, '.log')
#
#     # ROOT_DIR/.log가 존재하지 않는다면
#     if not os.path.exists(LOG_DIR):
#         # 만들어준다.
#         os.mkdir(LOG_DIR)

if not os.path.exists(LOG_DIR):
    LOG_DIR = os.path.join(ROOT_DIR, '.log')
    os.makedirs(LOG_DIR, exist_ok=True)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'django.server',
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
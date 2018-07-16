from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'django_extensions',
    'storages',
]
WSGI_APPLICATION = 'config.wsgi.dev.application'

DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'

DATABASES = secrets['DATABASES']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']


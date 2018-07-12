from .base import *

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
WSGI_APPLICATION = 'config.wsgi.local.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ALLOWED_HOSTS = [
    'localhost',
    '.amawonaws.com',
    '127.0.0.1',
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

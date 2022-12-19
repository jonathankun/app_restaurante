from .base import *  # noqa: F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u18pt4f^u%(93fu@)fow50b#u$ytx!$-a^mr5o%bv#yi_14)oq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_app_restaurante',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',  # localhost,'127.0.0.1'
        'PORT': '5432',  # 5432

    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR = [
    BASE_DIR / 'static',  # noqa: F405
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405
from common import *
import os

ROOTDIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'DungeonMaster',   # Or path to database file if using sqlite3.
        'USER': 'MrJew',                 # Not used with sqlite3.
        'PASSWORD': 'locked1337',       # Not used with sqlite3.
        'HOST': '',           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
    }
}

ROOT_URLCONF = 'dungeonMaster.urls'

TEMPLATE_DIRS = (
    '/home/mrjew/django_projects/dungeonMaster/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'system',
	'gm',
	'character',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

STATICFILES_DIRS = (
    '/home/mrjew/django_projects/dungeonMaster/static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MIDDLEWARE_CLASSES = (
    # ...

    # ...
    )

INTERNAL_IPS = ('127.0.0.1',)



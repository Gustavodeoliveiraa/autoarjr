from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-(0+0tm+s^7x#y+0)eu5(+)foo$vl0p)tv$!jojd3g5&l%_9ir*'

DEBUG = True

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-(0+0tm+s^7x#y+0)eu5(+)foo$vl0p)tv$!jojd3g5&l%_9ir*'

DEBUG = True if os.environ.get('DEBUG') == '1' else False

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

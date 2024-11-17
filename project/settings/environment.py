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

SESSION_COOKIE_AGE = 30 * 24 * 60 * 60  # 30 days in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = '/client/list'
LOGOUT_REDIRECT_URL = '/account/login'


# debug toolbar

INTERNAL_IPS = [
    "127.0.0.1",
]

# django channels
ASGI_APPLICATION = 'project.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',  # Use o Redis como backend
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],  # Conecta-se ao Redis local (padrão)
        },
    },
}
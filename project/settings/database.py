import os
from dotenv import load_dotenv
from .environment import BASE_DIR

load_dotenv()

debug_mode = os.environ.get('DEBUG', '0')

if debug_mode == '1':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

if debug_mode == '0':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('USER'),
            'PASSWORD': os.environ.get('PASSWORD'),
            'HOST': os.environ.get('HOST'),
            'PORT': os.environ.get('PORT')
        }
    }
print("Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

print(f"USER: {os.getenv('USER')}")

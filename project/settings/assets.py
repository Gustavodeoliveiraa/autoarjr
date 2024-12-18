import os
from project.settings.environment import BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

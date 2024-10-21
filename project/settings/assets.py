import os
from project.settings.environment import BASE_DIR

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

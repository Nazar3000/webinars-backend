from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ""
EMAIL_HOST_USER = 'no-reply@foxery.io'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

TEMPLATES[0]['DIRS'] += [os.path.join(BASE_DIR, 'chat/templates')]

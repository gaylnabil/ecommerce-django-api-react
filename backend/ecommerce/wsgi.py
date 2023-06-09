"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# application = get_wsgi_application()

application = get_wsgi_application()

application = WhiteNoise(application)

application.add_files(settings.STATIC_ROOT, prefix='static/')
application.add_files(settings.MEDIA_ROOT, prefix='media/')

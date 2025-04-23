"""
WSGI config for MenuBackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Default to development settings if not specified
# Production environments should set DJANGO_SETTINGS_MODULE explicitly
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MenuBackend.settings.dev")

application = get_wsgi_application()

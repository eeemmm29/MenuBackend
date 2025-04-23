"""
ASGI config for MenuBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Default to development settings if not specified
# Production environments should set DJANGO_SETTINGS_MODULE explicitly
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MenuBackend.settings.dev")

application = get_asgi_application()

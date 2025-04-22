import os
import environ
from pathlib import Path

# Define BASE_DIR locally first
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Create a temporary Env instance and read the .env.dev file
# This loads variables into os.environ
environ.Env.read_env(os.path.join(BASE_DIR, ".env.dev"))

# Now import base settings. The env instance in base.py will read from os.environ
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# Use env.bool from the base settings' env instance
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# Use env.list for ALLOWED_HOSTS, default to localhost for dev
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Use env() for database settings, providing defaults for SQLite in dev
DATABASES = {
    # Use env.db() which reads the DATABASE_URL environment variable
    # Or configure individual parts if DATABASE_URL is not set
    "default": env.db("DATABASE_URL", default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
    # Example for individual parts (if not using DATABASE_URL):
    # "default": {
    #     "ENGINE": env("DB_ENGINE", default="django.db.backends.sqlite3"),
    #     "NAME": env("DB_NAME", default=BASE_DIR / "db.sqlite3"),
    # }
}

# CORS settings for development
CORS_ALLOW_ALL_ORIGINS = True  # Keep allowing all for simplicity in dev
# Alternatively, use env.list for specific dev origins:
# CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=['http://localhost:3000', 'http://127.0.0.1:3000'])

# Optional: Add development-specific apps like django-debug-toolbar
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# INTERNAL_IPS = ['127.0.0.1']

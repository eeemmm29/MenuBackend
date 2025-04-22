import os
import environ
from pathlib import Path

# Define BASE_DIR locally first
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Create a temporary Env instance and read the .env.prod file
# This loads variables into os.environ
environ.Env.read_env(os.path.join(BASE_DIR, ".env.prod"))

# Now import base settings. The env instance in base.py will read from os.environ
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY is read in base.py

# SECURITY WARNING: don't run with debug turned on in production!
# Use env.bool from the base settings' env instance
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# Load allowed hosts from environment variable, required for production
# Use env.list, environ raises ImproperlyConfigured if missing and no default.
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Configure database for production using DATABASE_URL environment variable
# Environ raises ImproperlyConfigured if DATABASE_URL is missing.
DATABASES = {"default": env.db("DATABASE_URL")}
# Remove manual checks for individual DB variables as env.db handles DATABASE_URL

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# CORS settings for production
# Use env.list, providing an empty list as default if not strictly required.
# If CORS must be configured, remove the default to make it mandatory.
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
# Remove manual checks as environ handles missing variables.

# Ensure JWT Signing Key is set in production
# JWT_SIGNING_KEY is already read in base.py using env('JWT_SIGNING_KEY')
# Environ raises ImproperlyConfigured if it's missing, so no need for manual check.
# SIMPLE_JWT["SIGNING_KEY"] is updated in base.py

# Add any other production-specific settings here
# For example, HTTPS settings, logging configuration, etc.
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # If behind a proxy
# SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
# SESSION_COOKIE_SECURE = env.bool('DJANGO_SESSION_COOKIE_SECURE', default=True)
# CSRF_COOKIE_SECURE = env.bool('DJANGO_CSRF_COOKIE_SECURE', default=True)

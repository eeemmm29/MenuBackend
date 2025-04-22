import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for production environment")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Load allowed hosts from environment variable, required for production
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")
if not ALLOWED_HOSTS or ALLOWED_HOSTS == [""]:
    raise ValueError("No DJANGO_ALLOWED_HOSTS set for production environment")


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Configure database for production (e.g., PostgreSQL) using environment variables
DB_ENGINE = os.getenv("DB_ENGINE")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

if not all([DB_ENGINE, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT]):
    raise ValueError(
        "Production database settings are not fully configured in environment variables."
    )

DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# CORS settings for production
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
if not CORS_ALLOWED_ORIGINS or CORS_ALLOWED_ORIGINS == [""]:
    # Default to empty list if not set, effectively disallowing CORS unless configured
    CORS_ALLOWED_ORIGINS = []
    # Or raise an error if CORS must be explicitly configured:
    # raise ValueError("No CORS_ALLOWED_ORIGINS set for production environment")

# Ensure JWT Signing Key is set in production
JWT_SIGNING_KEY = os.getenv("JWT_SIGNING_KEY")
if not JWT_SIGNING_KEY:
    raise ValueError("No JWT_SIGNING_KEY set for production environment")

SIMPLE_JWT["SIGNING_KEY"] = JWT_SIGNING_KEY

# Add any other production-specific settings here
# For example, HTTPS settings, logging configuration, etc.
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

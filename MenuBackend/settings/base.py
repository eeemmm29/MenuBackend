"""
Django settings for MenuBackend project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import environ
from datetime import timedelta
from pathlib import Path
import cloudinary

# Remove get_random_secret_key import as environ handles default generation if needed
# from django.core.management.utils import get_random_secret_key

# Initialize django-environ
env = environ.Env(
    # set casting, default value
    DJANGO_DEBUG=(bool, False)
)

cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# environ.Env.read_env(os.path.join(BASE_DIR, '.env')) # Reading .env moved to dev/prod

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Environ will raise ImproperlyConfigured if SECRET_KEY is not found in prod
SECRET_KEY = env("SECRET_KEY")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",  # add if you want social authentication
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "corsheaders",
    "django_filters",
    "authentication",
    "menu",
    "favorites",
    "cloudinary",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # The SessionAuthentication class enables the browsable API to use Django's session framework for authentication
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_VERSION": "v1",
    "ALLOWED_VERSIONS": ["v1"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    # From djangorestframework-camel-case
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
        # Any other renders
    ),
    "DEFAULT_PARSER_CLASSES": (
        # If you use MultiPartFormParser or FormParser, we also have a camel case version
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
        # Any other parsers
    ),
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "djangorestframework_camel_case.middleware.CamelCaseMiddleWare",
]

ROOT_URLCONF = "MenuBackend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "MenuBackend.wsgi.application"

APPEND_SLASH = False


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Database configuration is now handled entirely in dev.py and prod.py using env()


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
# STATIC_ROOT is environment-specific, defined in prod.py using env()

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Media files configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Optional: Allow credentials (cookies, authorization headers)
CORS_ALLOW_CREDENTIALS = True
# CORS origin settings moved to dev.py and prod.py using env()

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    # Environ will raise ImproperlyConfigured if JWT_SIGNING_KEY is not found in prod
    "SIGNING_KEY": env("JWT_SIGNING_KEY"),
    "ALGORITHM": "HS512",
}

SITE_ID = 1  # make sure SITE_ID is set

# ACCOUNT_SIGNUP_FIELDS = ["username", "password1", "password2"]
ACCOUNT_EMAIL_VERIFICATION = "none"

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
    "JWT_AUTH_RETURN_EXPIRATION": True,
    "USER_DETAILS_SERIALIZER": "authentication.serializers.UserSerializer",
}

# DEBUG and ALLOWED_HOSTS are handled in dev.py/prod.py using env()
# Database settings are handled in dev.py/prod.py using env()
# CORS settings are handled in dev.py/prod.py using env()

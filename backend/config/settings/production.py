from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# PostgreSQL (Render will give you this)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# Security (IMPORTANT)
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files (Render-friendly)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Optional: CORS for frontend later
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ORIGINS", "").split(",")
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DEV_NAME"),
        "USER": os.getenv("DEV_USER"),
        "PASSWORD": os.getenv("DEV_PASSWORD"),
        "HOST": os.getenv("DEV_HOST"),
        "PORT": os.getenv("DEV_PORT"),
    }
}


CORS_ALLOW_ALL_ORIGINS = True
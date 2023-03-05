from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    },
}


STATICFILES_DIRS = [os.path.join(os.path.dirname("settings"), "static")]
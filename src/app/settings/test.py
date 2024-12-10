import logging

from .common import *  # noqa

SECRET_KEY = "django-test"

# Core
logging.disable(logging.CRITICAL)
DEBUG = False
TEMPLATE_DEBUG = False

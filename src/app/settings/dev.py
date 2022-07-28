from .common import * #noqa

# Core
DEBUG = DEBUG_TOOLBAR = True
INSTALLED_APPS += [
    'drf_yasg'
]

# Swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}


# Hosting and CORS
CORS_ALLOWED_ORIGINS = ()
ALLOWED_HOSTS += []
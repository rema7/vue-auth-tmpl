import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
LOG_LEVEL = 'ERROR'

AUTH_CODE_VALID_DURATION = 300

# DB SECTION
DB_CONNECTION = 'postgresql+psycopg2://localhost/gisrdm_db'
DISABLE_SIGNUP = True

try:
    from settings_local import *
except ModuleNotFoundError:
    pass

# FRONTEND
FURL_SPACE_SETTINGS = '/api/space_settings'

FURL_LOGIN = '/api/auth/login'
FURL_REGISTER = '/api/auth/register'

FURL_ACCOUNT = '/api/account'


# BACKEND SECTION
SETTINGS_ROUTE = '/settings'
LOGIN_ROUTE = '/auth/login'
REGISTER_ROUTE = '/auth/register'

ACCOUNT_ROUTE = '/account'

DB_CONNECTION_YOYO = DB_CONNECTION.replace('+psycopg2', '')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['debug_file'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'stream': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'debug_file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_DIR, 'debug.logs'),
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_DIR, 'error.logs'),
        },
        'access_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'access.logs'),
        }
    },
    'loggers': {
        'worker': {
            'level': LOG_LEVEL,
            'handlers': ['stream'],
        },
        'rema-rest': {
            'level': LOG_LEVEL,
            'handlers': ['error_file', 'debug_file'],
            'propagate': False,
        },
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['error_file'],
            'propagate': True,
        },
        'gunicorn.access': {
            'level': 'INFO',
            'handlers': ['access_file'],
            'propagate': False,
        },
    },
}

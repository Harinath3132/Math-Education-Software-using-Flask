import os
import logging

LOG_LEVEL = logging.DEBUG
PRESERVE_CONTEXT_ON_EXCEPTION = True
DEBUG = False

SESSION_COOKIE_SAMESITE = 'strict'
SESSION_COOKIE_PATH = '/uncg_math'
SESSION_KEY_PREFIX = "hello"
SESSION_COOKIE_NAME = "uncg_math_session"


ROOT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
TEMP_DIR = os.path.join(ROOT_DIR, 'temp')

DIRECTORIES = [LOG_DIR, TEMP_DIR]


SECRET_KEY = "Kc5c3zTk'-3<&BdL:P92O{_(:-NkY+"

ENVIRONMENT = "development"

MYSQL_CHARSET = 'utf8mb4'

PROPAGATE_EXCEPTIONS = True

CORS_HEADERS = [
    'Content-Type',
    'Authorization'
]

CORS_ORIGIN_WHITELIST = [
'127.0.0.1:5000'
]

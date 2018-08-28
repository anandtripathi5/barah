import os

import sys

FLASK_APP_NAME = os.environ.get("FLASK_APP_NAME")
DEBUG = os.environ.get("FLASK_DEBUG")
DATABASE_URL = os.environ.get("DATABASE_URL")
# SECRET_KEY = "my_secret_key"

DEFAULT_LOGGER_NAME = os.environ.get("DEFAULT_LOGGER_NAME")
LOGGING_CONFIG = dict(
    version=1,
    filters={
        'request_id': {
            '()': 'utils.log_utils.RequestIdFilter',
        },
    },
    formatters={
        'compact': {
            'format': '%(request_id)s - %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - [%(levelname)s] - %(message)s'
        },
        'err_report': {'format': '%(asctime)s\n%(message)s'}
    },
    handlers={
        DEFAULT_LOGGER_NAME: {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'compact',
            'filters': ['request_id'],
            'level': 'DEBUG',
            # 'filename': os.environ.get("DEFAULT_LOGGER_FILE_NAME"),
            # 'interval': 1,
            # 'when': 'midnight',
            # 'encoding': 'utf8'
        },
        'sm_lib': {
            'class': 'logging.StreamHandler',
            'formatter': 'compact',
            'filters': ['request_id'],
            'level': 'DEBUG',
            # 'filename': os.environ.get("SM_LIB_LOGGER_FILE_NAME"),
            # 'interval': 1,
            # 'when': 'midnight',
            # 'encoding': 'utf8'
        },
        'critical_err': {
            'class': 'logging.handlers.SMTPHandler',
            'formatter': 'err_report',
            'mailhost': ("localhost", 25),
            'fromaddr': 'a@a.com',
            'toaddrs': [
                'a@a.com'
            ],
            'subject': 'OneAPI : Something bad happened'
        }
    },
    loggers={
        DEFAULT_LOGGER_NAME: {
            'handlers': [DEFAULT_LOGGER_NAME],
            'level': 'DEBUG',
            'propagate': False
        },
        'crash': {
            'handlers': ['critical_err', DEFAULT_LOGGER_NAME],
            'level': 'ERROR',
            'propagate': False
        },
    }
)

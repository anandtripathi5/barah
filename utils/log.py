import logging
import sys
import uuid

import flask
from flask import Flask

from config import settings

_formatter = '%(rid)s - %(asctime)s - %(filename)s - %(module)s - %(funcName)s - ' \
             '%(lineno)s - [%(levelname)s] - %(message)s'


class ContextFilter(logging.Filter):
    '''Enhances log messages with request_id information'''

    def filter(self, record):
        self._add_rid(record)
        return True

    @staticmethod
    def _add_rid(record):
        if not hasattr(flask.g, 'rid'):
            uuid_value = uuid.uuid4()
            flask.g.rid = uuid_value
            record.rid = uuid_value
        else:
            record.rid = flask.g.rid


def configure_logging(app: Flask):
    handle = logging.StreamHandler(sys.stdout)
    handle.setLevel(settings.LOG_LEVEL)
    handle.addFilter(ContextFilter())
    formatter = logging.Formatter(_formatter)
    handle.setFormatter(formatter)
    app.logger.handlers = []
    app.logger.addHandler(handle)
    app.logger.setLevel(settings.LOG_LEVEL)

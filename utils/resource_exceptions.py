from functools import wraps
from flask_restful import abort
from models import session
from flask import current_app as app


def handle_exceptions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValueError as val_err:
            app.logger.error(val_err)
            session.rollback()
            return abort(400, message=val_err.message)
        except KeyError as key_err:
            app.logger.error(key_err)
            session.rollback()
            return abort(400, message=key_err.message)
        except IOError as io_err:
            app.logger.error()
            session.rollback()
            return abort(500, message=io_err.message)
        except Exception as exc:
            app.logger.error(exc)
            session.rollback()
            abort(500, message=exc.message)

    return wrapper

from functools import wraps
from flask import current_app as app


def function_logger(func):
    @wraps(func)
    def function_log(*args,     **kwargs):
        app.logger.debug(
            "Inside Function {} with parameters: {},{}".format(
                func.__name__,
                args,
                kwargs
            )
        )
        return_param = func(*args, **kwargs)
        app.logger.debug(
            "Function: {} returns {}".format(
                func.__name__,
                return_param
            )
        )
        return return_param
    return function_log
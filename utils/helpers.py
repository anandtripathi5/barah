from functools import wraps

from flask_jwt_extended import jwt_required, current_user
from flask_jwt_extended.exceptions import JWTExtendedException


def auth_required(permission):
    def decorator(function):
        @wraps(function)
        @jwt_required()
        def wrapper(*args, **kwargs):
            if current_user.permission != permission:
                raise JWTExtendedException("User not allowed")
            result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator

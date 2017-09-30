from flask import current_app as app
from flask_restful import Resource

from utils.resource_exceptions import handle_exceptions


class HelloWorld(Resource):
    decorators = [handle_exceptions]

    def __init__(self):
        app.logger.debug(
            'In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        return "hello world"

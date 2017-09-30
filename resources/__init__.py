from flask_cors import CORS
from flask_restful import Api

from resources.hello_world import HelloWorld


def restful_api(app):
    CORS(app, resources={r"/*": {"origins": "*"}})

    api = Api(app, prefix="/api")
    api.add_resource(HelloWorld, '/hello_world')

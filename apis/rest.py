from extensions import db, docs, jwt
from flask_restful import Api

from apis.urls import urls
from apis.users.models import User

api = Api()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return db.query(User).filter(User.id == identity).one_or_none()


def init_routes(app):
    for url in urls:
        api.add_resource(url.resource, url.url)
        app.add_url_rule(url.url, view_func=url.resource.as_view(url.url[1:]))
        docs.register(url.resource)

from extensions import db, security_params
from flask_apispec import MethodResource, doc, use_kwargs
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from flask_restful import Resource
from marshmallow import Schema
from webargs import fields

from apis.users.models import User


class SignupRequest(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class LoginRequest(Schema):
    username = fields.Email(required=True)
    password = fields.String(required=True)
    grant_type = fields.String(missing=True)


class Signup(MethodResource, Resource):

    @doc(description="Signup User API call", tags=["User"])
    @use_kwargs(SignupRequest)
    def post(self, **kwargs):
        obj = User(**kwargs)
        db.add(obj)
        return dict(message="User Added")


class Login(MethodResource, Resource):

    @doc(description="Login API call", tags=["User"])
    @use_kwargs(LoginRequest, location=('form'))
    def post(self, username=None, password=None, grant_type=None):
        user = db.query(User).filter(User.email == username).first()
        if not user:
            raise ValueError("User not found")
        if user.password != password:
            raise ValueError("password doesn't match")

        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)

        return dict(access_token=access_token, refresh_token=refresh_token)


class Refresh(MethodResource, Resource):

    @doc(description="Refresh API call", tags=["User"],
         security=security_params)
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return dict(access_token=access_token)

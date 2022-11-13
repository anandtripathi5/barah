from extensions import db, security_params
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_restful import Resource
from marshmallow import Schema
from utils.helpers import auth_required
from webargs import fields

from apis.books.models import Book
from apis.users.models import PermissionEnum


class BookModel(Schema):
    name = fields.String(required=True)
    description = fields.String(required=False)


class BooksResponse(Schema):
    books = fields.List(fields.Nested(BookModel))
    message = fields.String()


class Books(MethodResource, Resource):

    @doc(description="Books namespace", tags=["Book"],
         security=security_params)
    @marshal_with(BooksResponse)
    @auth_required(PermissionEnum.admin)
    def get(self):
        books = db.query(Book).all()
        return dict(books=books, message="success"), 200

    @doc(description="Books namespace", tags=["Book"])
    @use_kwargs(BookModel, location=('json'))
    @auth_required(PermissionEnum.admin)
    def put(self, name=None, description=None):
        book = Book(name=name, description=description)
        db.add(book)
        db.flush()
        return dict(id=book.id, message="Book added"), 202

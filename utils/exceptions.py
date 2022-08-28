from flask_jwt_extended.exceptions import JWTExtendedException
from werkzeug.exceptions import UnprocessableEntity, Unauthorized


class ExcHandlers():
    def __init__(self, db):
        self.db = db

    def init_app(self, app):
        @app.errorhandler(ValueError)
        def value_error(e):
            self.db.rollback()
            return dict(message="Value Error", exc_info=str(e)), 400

        @app.errorhandler(UnprocessableEntity)
        def unprocess(e):
            return dict(message="Input Error",
                        exc_info=e.data['messages']), 400

        @app.errorhandler(JWTExtendedException)
        @app.errorhandler(Unauthorized)
        def unauthorized(e):
            return dict(message="Unauthorized error", exc_info=str(e)), 401

        @app.errorhandler(Exception)
        def general_error(e):
            self.db.rollback()
            return dict(message="Exception", exc_info=str(e)), 500

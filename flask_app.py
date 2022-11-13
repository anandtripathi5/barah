from flask import Flask

from apis.rest import api, init_routes
from config import settings
from extensions import db, docs, exc, jwt, session
from utils.log import configure_logging


def create_app():
    # flask app configuration
    app = Flask(__name__)
    app.config.from_object(settings)
    configure_logging(app)
    api.init_app(app)
    exc.init_app(app)
    docs.init_app(app)
    init_routes(app)
    jwt.init_app(app)
    return app


app = create_app()

app.app_context().push()


# This gets called after each request
@app.teardown_request
def teardown_request(response_or_exc):
    if response_or_exc:
        db.rollback()
    else:
        db.commit()
    session.remove()


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    session.commit()
    session.remove()


if __name__ == '__main__':
    app.run(debug=True, port=8000)

import logging.config

from flask import Flask

import resources
from config import FLASK_APP_NAME
from constants.common_constants import FLASK_CONFIG
from helper import config_logger
from models import get_session


def create_app():
    # flask app configuration
    app = Flask(FLASK_APP_NAME)
    app.config.from_object(FLASK_CONFIG)

    # database session
    database_url = app.config.get("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE-URL-NOT-SET")
    session = get_session(database_url=database_url)

    # logger configuration
    config_logger(app)
    resources.restful_api(app)

    # teardown database session
    def close_session(response_or_exc):
        session.remove()
        return response_or_exc

    app.teardown_appcontext(close_session)
    return app

main_app = create_app()
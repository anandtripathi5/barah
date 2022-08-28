from flask_apispec import FlaskApiSpec
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy_utils import force_auto_coercion

from config import settings
from utils.exceptions import ExcHandlers

session = scoped_session(
    sessionmaker(bind=create_engine(settings.DATABASE_URL))
)
db: Session = session()
Base = declarative_base()
exc = ExcHandlers(db)
docs = FlaskApiSpec()
security_params = [{"bearer": []}]
jwt = JWTManager()

force_auto_coercion()

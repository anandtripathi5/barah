from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

session = None


def get_session(database_url=None):
    if session:
        return session

    session_obj = sessionmaker(bind=create_engine(database_url))
    session = scoped_session(session_obj)
    global session
    return session

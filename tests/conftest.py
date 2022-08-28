import pytest
from flask_webtest import TestApp

from extensions import db as _db, session
from flask_app import app as _app


@pytest.fixture(autouse=True)
def db(request, monkeypatch):
    # Roll back at the end of every test\
    request.addfinalizer(_db.rollback)
    request.addfinalizer(session.remove)

    # committing (redirect to flush() instead)
    monkeypatch.setattr(_db, 'commit', _db.flush)

    return _db


@pytest.fixture(autouse=True)
def test_app(db):
    return TestApp(_app, db=db)

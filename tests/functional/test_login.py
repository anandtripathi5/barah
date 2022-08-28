import pytest

from apis.users.models import User


class TestLogin(object):

    @pytest.fixture(autouse=True)
    def setup(self, test_app, db):
        self.test_app = test_app
        self.db = db
        obj = User(name='Anand', email="test@gmail.com", password="root")
        self.db.add(obj)
        self.db.flush()

    def test_login(self):
        res = self.test_app.post("/login",
                                 dict(username="anand@gmail.com",
                                      password="root"),
                                 expect_errors=True,
                                 content_type="application/x-www-form-urlencoded")
        assert res.status_code == 200
        assert res.json['access_token']
        assert res.json['refresh_token']

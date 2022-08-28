from apis.books.views import Books
from apis.users.views import Signup, Refresh, Login


class API:
    def __init__(self, resource, url):
        self.resource = resource
        self.url = url


urls = [
    API(Books, '/books'),
    API(Signup, '/signup'),
    API(Login, '/login'),
    API(Refresh, '/refresh'),
]

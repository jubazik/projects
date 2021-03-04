from api import api, app
from api.endpoints.quotes.resource import QuoteResource
from api.endpoints.authors.resource import AuthorResource
from config import Config

api.add_resource(QuoteResource,
                 '/author/<int:author_id>/quotes/',
                 '/author/<int:author_id>/quotes/<int:quote_id>'
                 )  # <-- requests
api.add_resource(AuthorResource, '/author/<int:author_id>/', '/author/')  # <-- requests

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

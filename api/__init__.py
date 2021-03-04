from config import Config
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from api.endpoints.quotes.model import QuoteModel
# from api.endpoints.authors.model import AuthorModel


class UnicodeApi(Api):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app.config['RESTFUL_JSON'] = {
            'ensure_ascii': False,
        }


app = Flask(__name__)
app.config.from_object(Config)
api = UnicodeApi(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

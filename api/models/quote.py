from api import db
from api.models.author import AuthorModel


class QuoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey(AuthorModel.id))
    quote = db.Column(db.String(255), unique=False)

    def __init__(self, author: AuthorModel, quote: str):
        self.author_id = author.id
        self.quote = quote

    def to_dict(self):
        return {
            "id": self.id,
            "quote": self.quote,
            "author": self.author.to_dict()
        }

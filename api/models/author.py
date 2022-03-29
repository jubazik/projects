from api import db


class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    surname = db.Column(db.String(64), nullable=False, server_default="Default")
    quotes = db.relationship('QuoteModel', backref='author', lazy='dynamic')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

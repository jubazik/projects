from api import db
from api.models.author import AuthorModel

class QuoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey(AuthorModel.id))
    text = db.Column(db.String(255), unique=False)

    def __init__(self, author: AuthorModel, text: str):
        self.author_id = author.id
        self.text = text

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "author": self.author.to_dict()
        }
# class Payments(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.DateTime, default=datetime.datetime.now())
#     cash = db.Column(db.TEXT, unique=False)
#     author_id = db.Column(db.Integer, db.ForeignKey(NameCard.id))
#     sun = db.Column(db.Integer, unique=False)
#     type = db.Column(db.String(32), unique=False)
#     comment = db.Column(db.Text, unique=False)
#
#     def __init__(self, cash, author, sun, type, comment):
#         self.cash = cash
#         self.author_id = author.id
#         self.sun = sun
#         self.type = type
#         self.comment = comment
#
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "date": self.date,
#             "cash": self.cash,
#             "name": self.author.to_dict(),
#             "sun": self.sun,
#             "type": self.type,
#             "comment": self.comment
#         }

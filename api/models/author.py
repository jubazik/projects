from api import db
# import datetime


class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    surname = db.Column(db.String(64), nullable=False, server_default="Default")
    quotes = db.relationship('QuoteModel', backref='author', lazy='dynamic')

    def __init__(self, name):
        self.name = name


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname
        }
# class NameCard(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Date, default=datetime.datetime.now())
#     name = db.Column(db.String(32), unique=True)
#     room = db.Column(db.String(32), unique=False)
#     sun = db.relationship('Payments', backref='author', lazy='dynamic')
#
#     def __init__(self, name, room = "Пусто"):
#         self.name = name
#         self.room = room
#
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "room": self.room
#         }
#
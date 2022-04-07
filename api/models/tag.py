from api import db
from api.models.mixins import ModelDBExt
from api.models.user import UserModel


class TagModel(db.Model, ModelDBExt):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    # author_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))

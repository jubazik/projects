from api import ma
from api.models.note import NoteModel
from api.schemas.user import UserSchema


#       schema        flask-restful
# object ------>  dict ----------> json

class NoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = NoteModel

    id = ma.auto_field()
    text = ma.auto_field()
    private = ma.auto_field()
    author = ma.Nested(UserSchema())


class NoteRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = NoteModel

    text = ma.Str(required=True)
    private = ma.Bool()


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)

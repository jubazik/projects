from webargs import fields
from flask_apispec.views import MethodResource
from flask_apispec import doc, marshal_with, use_kwargs
from api.models.note import NoteModel
from api.schemas.note import NoteSchema
from api.models.tag import TagModel
from api.schemas.tag import TagSchema, TagRequestSchema


@doc(tags=["Tags"])
class TagResource(MethodResource):
    @marshal_with(TagSchema, code=200)
    def get(self, tag_id):
        tag = TagModel.query.get(tag_id)
        if tag is None:
            return {"error": f"Tag with id={tag_id} not found"}, 404
        return tag, 200


@doc(tags=["Tags"])
class TagsListResource(MethodResource):
    @marshal_with(TagSchema(many=True), code=200)
    def get(self):
        tags = TagModel.query.all()
        return tags, 200
    
    @use_kwargs(TagRequestSchema, location='json')
    @marshal_with(TagSchema, code=201)
    def post(self, **kwargs):
        tag = TagModel(**kwargs)
        tag.save()
        return tag, 201

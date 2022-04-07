from werkzeug.exceptions import NotFound
from flask_babel import _


def get_object_or_404(model, obj_id):
    obj = model.query.get(obj_id)
    if obj is None:
        raise NotFound(description=_("... with id=%(obj_id)s not found", obj_id=obj_id))
    return obj

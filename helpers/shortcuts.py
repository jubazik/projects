from werkzeug.exceptions import NotFound


def get_object_or_404(model, obj_id):
    obj = model.query.get(obj_id)
    if obj is None:
        raise NotFound(description=f"... with id={obj_id} not found")
    return obj

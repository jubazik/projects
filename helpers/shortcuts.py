def get_object_or_404(model, obj_id):
    obj = model.query.get(obj_id)
    if obj is None:
        return {"error": f"... with id={obj_id} not found"}, 404
    return obj

import json
from api import db
from api.schemas.user import UserRequestSchema
from config import BASE_DIR, base_dir
from sqlalchemy.exc import IntegrityError

from api.models.note import NoteModel
from api.models.user import UserModel

# path_to_fixture = os.path.join(base_dir, "fixtures", "users.json")
path_to_fixture = BASE_DIR / "fixtures" / "notes.json"
models = {
    "NoteModel": NoteModel,
    "UserModel": UserModel,
}
with open(path_to_fixture, "r", encoding="UTF-8") as f:
    data = json.load(f)
    users_created = 0
    model_name = data["model"]
    model = models[model_name]
    for record in data["records"]:
        model_object = model(**record)
        model_object.save()

    print(f"??? users created")

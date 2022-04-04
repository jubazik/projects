import os
from api import db
from api.schemas.user import UserRequestSchema
from config import BASE_DIR, base_dir

from api.models.note import NoteModel
from api.models.user import UserModel

# path_to_fixture = os.path.join(base_dir, "fixtures", "users.json")
path_to_fixture = BASE_DIR / "fixtures" / "users.json"
with open(path_to_fixture, "r", encoding="UTF-8") as f:
    users_data = UserRequestSchema(many=True).loads(f.read())
    
    for user_data in users_data:
        user = UserModel(**user_data)
        db.session.add(user)
    db.session.commit()
    print(f"{len(users_data)} users created")

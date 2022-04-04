import os
from api import db
from api.schemas.user import UserRequestSchema
from config import BASE_DIR, base_dir
from sqlalchemy.exc import IntegrityError

from api.models.note import NoteModel
from api.models.user import UserModel

# path_to_fixture = os.path.join(base_dir, "fixtures", "users.json")
path_to_fixture = BASE_DIR / "fixtures" / "users.json"
with open(path_to_fixture, "r", encoding="UTF-8") as f:
    users_data = UserRequestSchema(many=True).loads(f.read())
    users_created = 0
    for user_data in users_data:
        user = UserModel(**user_data)
        db.session.add(user)
        try:
            db.session.commit()
            users_created += 1
        except IntegrityError:
            db.session.rollback()
            print(f"User {user.username} already exists")

    print(f"{users_created} users created")

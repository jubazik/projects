from api import Resource, reqparse, db
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema


# url: /users/<int:user_id>
class UserResource(Resource):
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if user is None:
            return {"error": "User not found"}, 404
        return user_schema.dump(user), 200


# url: /users
class UsersListResource(Resource):
    def get(self):
        users = UserModel.query.all()
        return users_schema.dump(users), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201

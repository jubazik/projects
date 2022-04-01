from api import Resource, abort, reqparse, auth, docs
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema, UserSchema, UserRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, use_kwargs, doc


@doc(tags=['Users'])
class UserResource(MethodResource):
    @marshal_with(UserSchema, code=200) # Сериализации
    @doc(summary='Get User by id')
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if user is None:
            abort(404, error=f"User with id={user_id} not found")
        return user, 200

    @auth.login_required(role="admin")
    @doc(summary='Edit User')
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        user_data = parser.parse_args()
        user = UserModel.query.get(user_id)
        user.username = user_data["username"]
        user.save()
        return user_schema.dump(user), 200

    @auth.login_required
    def delete(self, user_id):
        raise NotImplemented  # не реализовано!


@doc(tags=["Users"])
class UsersListResource(MethodResource):
    @doc(summary="Get all users")
    @marshal_with(UserSchema(many=True), code=200)
    def get(self):
        users = UserModel.query.all()
        return users, 200

    @doc(summary="Create new User")
    @marshal_with(UserSchema, code=201)
    @use_kwargs(UserRequestSchema, location='json')
    def post(self, **kwargs):
        user = UserModel(**kwargs)
        user.save()
        if not user.id:
            abort(400, error=f"User with username:{user.username} already exist")
        return user, 201

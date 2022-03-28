from api import Resource, reqparse, db
from api.models.author import AuthorModel


# GET: /authors/1 - author by id
class AuthorResource(Resource):
    def get(self, author_id):
        author = AuthorModel.query.get(author_id)
        if author is None:
            return f"Author id={author_id} not found", 404

        return author.to_dict(), 200

    def put(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        author_data = parser.parse_args()
        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404
        author.name = author_data["name"]
        db.session.commit()
        return author.to_dict(), 200

    def delete(self, quote_id):
        raise NotImplemented("Метод не реализован")


# GET: /authors - authors list
class AuthorsListResource(Resource):
    def get(self):
        authors = AuthorModel.query.all()
        authors_list = [author.to_dict() for author in authors]
        return authors_list, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        author_data = parser.parse_args()
        author = AuthorModel(author_data["name"])
        db.session.add(author)
        db.session.commit()
        return author.to_dict(), 201

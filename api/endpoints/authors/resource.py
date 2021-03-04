from api import Resource, reqparse, db
from api.endpoints.authors.model import AuthorModel


class AuthorResource(Resource):
    def get(self, author_id=0):
        if id == 0:
            authors = AuthorModel.query.all()
            authors_list = [author.to_dict() for author in authors]
            return authors_list, 200

        author = AuthorModel.query.get(author_id)
        if author is not None:
            return author.to_dict(), 200
        return f"Author id={author_id} not found", 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        author_data = parser.parse_args()
        author = AuthorModel(author_data["name"])
        db.session.add(author)
        db.session.commit()
        return author.to_dict(), 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        author_data = parser.parse_args()
        author = AuthorModel.query.get(id)
        if author is None:
            author = AuthorModel(author_data["name"])
            db.session.add(author)
            db.session.commit()
            return author.to_dict(), 201
        author.name = author_data["name"]
        db.session.commit()
        return author.to_dict(), 200

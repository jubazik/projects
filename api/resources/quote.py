from api import Resource, reqparse, db
from api.models.author import AuthorModel
from api.models.quote import QuoteModel


class QuoteResource(Resource):
    def get(self, author_id=None, quote_id=None):
        """
        Обрабатываем GET запросы
        :param id: id цитаты
        :return: http-response("текст ответа", статус)
        """
        if author_id is None and quote_id is None:
            quotes = QuoteModel.query.all()
            return [quote.to_dict() for quote in quotes]

        author = AuthorModel.query.get(author_id)
        if quote_id is None:
            quotes = author.quotes.all()
            return [quote.to_dict() for quote in quotes], 200

        quote = QuoteModel.query.get(id)
        if quote is not None:
            return quote.to_dict(), 200
        return {"Error": "Quote not found"}, 404

    def post(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("quote", required=True)
        quote_data = parser.parse_args()
        author = AuthorModel.query.get(author_id)
        if author:
            quote = QuoteModel(author, quote_data["quote"])
            db.session.add(quote)
            db.session.commit()
            return quote.to_dict(), 201
        return {"Error": f"Author id={author_id} not found"}, 404

    def put(self, quote_id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        new_data = parser.parse_args()

        quote = QuoteModel.query.get(quote_id)
        quote.author = new_data["author"]
        quote.quote = new_data["quote"]
        db.session.commit()
        return quote.to_dict(), 200

    def delete(self, quote_id):
        quote = QuoteModel.query.get(quote_id)
        if quote is None:
            return f"Quote with id {quote_id} not found", 404
        db.session.delete(quote)
        db.session.commit()
        return quote.to_dict(), 200

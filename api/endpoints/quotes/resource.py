from api import Resource, reqparse, db
from api.endpoints.authors.model import AuthorModel
from api.endpoints.quotes.model import QuoteModel


class QuoteResource(Resource):
    def get(self, author_id, quote_id=0):
        """
        Обрабатываем GET запросы
        :param id: id цитаты
        :return: http-response("текст ответа", статус)
        """
        author = AuthorModel.query.get(author_id)
        if quote_id == 0:
            quotes = author.quotes.all()
            quotes_list = [quote.to_dict() for quote in quotes]
            return quotes_list, 200

        quote = QuoteModel.query.get(id)
        if quote is not None:
            return quote.to_dict(), 200
        return "Quote not found", 404

    def post(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("quote")
        quote_data = parser.parse_args()
        author = AuthorModel.query.get(author_id)
        quote = QuoteModel(author, quote_data["quote"])
        db.session.add(quote)
        db.session.commit()
        return quote.to_dict(), 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        new_data = parser.parse_args()

        quote = QuoteModel.query.get(id)
        quote.author = new_data["author"]
        quote.quote = new_data["quote"]
        db.session.commit()
        return quote.to_dict(), 200

    def delete(self, id):
        quote = QuoteModel.query.get(id)
        if quote is None:
            return f"Quote with id {id} not found", 404
        db.session.delete(quote)
        db.session.commit()
        return quote.to_dict(), 200
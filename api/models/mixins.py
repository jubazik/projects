from api import db
from sqlalchemy.exc import IntegrityError


class ModelDBExt:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:  # Обработка ошибки "создание пользователя с НЕ уникальным именем"
            db.session.rollback()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

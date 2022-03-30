import json
from api import db
from app import app
from unittest import TestCase
from api.models.user import UserModel
from config import Config


class TestUsers(TestCase):
    def setUp(self):
        """
        Данный метод запускается перед КАЖДЫМ тестом
        """
        self.app = app
        # Клиент для отправки запросов
        self.client = self.app.test_client()
        self.app.config.update({
            'SQLALCHEMY_DATABASE_URI': Config.TEST_DATABASE_URI
        })

        with self.app.app_context():
            # Создаем таблицы в БД
            db.create_all()

    def test_users_get(self):
        """
        Тест на получения списка пользователей
        """
        users_data = [
            {
                "username": 'admin',
                'password': 'admin'
            },
            {
                "username": 'ivan',
                'password': '1234'
            },
        ]
        for user_data in users_data:
            user = UserModel(**user_data)
            db.session.add(user)
        db.session.commit()
        response = self.client.get("/users")
        data = json.loads(response.data)
        self.assertEqual(users_data[0]["username"], data[0]["username"])
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("password", data[0].keys())

    def test_user_creation(self):
        """
        Тест на создание нового пользователя
        """
        user_data = {
            "username": 'admin',
            'password': 'admin'
        }
        ...

    def tearDown(self):
        """
        Данный метод запускается после КАЖДОГО теста
        """
        with self.app.app_context():
            # Удаляем все таблицы в БД
            db.session.remove()
            db.drop_all()

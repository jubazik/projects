# Развертывание на локальной машине
1. Создаем виртуальное окружение: python3 -m venv flask_venv
2. Активируем venv: source flask_venv/bin/activate
3. Устанавливаем зависимости: pip install -r requirements.txt
4. Создаем локальную БД: flask db upgrade

# Миграции
1. Активировать миграции: flask db init
2. Создать миграцию: flask db migrate -m "comment"
3. Применить миграции: flask db upgrade

# Переменные окружение
1. Установить утилиту для работы с env: sudo apt install direnv
2. Разрешить установку переменных окружения: direnv allow .
3. Запуск проекта: flask run
# Новостной сайт
сайт с новостями, базой данных, отзывами, отправкой файлов. Новости, отзывы можно добавлять. Автоматическое отображение. Стили css, javascript.

## Технологии
Использовали Flask, sqlite3, flask-wtf(flask forms)

## Как запустить
1. Клонируем репозиторий
'''comandline
git clone https://github.com/Phoolore/Flask.git
'''
2. Создаем виртуальное окружение
'''comandline
python -m venv vertualenv
'''
3. Устанавливаем зависимости(фреймворки, пакеты)
'''comandline
pip install -r requirements.txt
'''
4. Создаем файл .env и укажите настройки подключения к БД(sqlite и т.п.) и т.п.
'''.env
DATABASE_URI = sqlite:///db.sqlite3

SECRET_KEY = YOUR_SECRET_KEY
'''
5. Запустите flask приложение
'''comandline
python -m flask run
'''
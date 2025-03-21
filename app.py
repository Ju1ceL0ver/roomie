from flask import Flask
from config import Config
from database import db, init_db
from routes import init_routes

app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных и маршрутов
init_db(app)
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
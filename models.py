from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.String(10), nullable=True)  # Например, "male", "female"
    password_hash = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    verified = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.Text, nullable=True)  # Описание пользователя
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    photo_url = db.Column(db.String(200), nullable=True)  # Ссылка на фото

    # Связь с объявлениями
    ads = db.relationship('Ad', backref='user', lazy=True)

    def to_dict(self):
        """Метод для сериализации объекта в словарь"""
        return {
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'age': self.age,
            'sex': self.sex,
            'email': self.email,
            'phone': self.phone,
            'verified': self.verified,
            'description': self.description,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'photo_url': self.photo_url  # Добавляем фото в сериализацию
        }

class Ad(db.Model):
    __tablename__ = 'ads'

    ad_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    entire_house = db.Column(db.Boolean, nullable=True)
    floor = db.Column(db.Integer, nullable=True)
    area = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        """Метод для сериализации объявления в словарь"""
        return {
            'ad_id': self.ad_id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'description': self.description,
            'price': self.price,
            'city': self.city,
            'location': self.location,
            'entire_house': self.entire_house,
            'floor': self.floor,
            'area': self.area
        }
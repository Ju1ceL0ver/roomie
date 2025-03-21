from flask import render_template, request, redirect, url_for, flash
from database import db
from models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def init_routes(app):
    bcrypt.init_app(app)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            password = request.form.get('password')

            if User.query.filter_by(email=email).first():
                return render_template('register.html', message="Этот email уже зарегистрирован")

            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password_hash=password_hash
            )
            db.session.add(new_user)
            db.session.commit()
            return render_template('register.html', message="Регистрация прошла успешно!")
        
        return render_template('register.html')
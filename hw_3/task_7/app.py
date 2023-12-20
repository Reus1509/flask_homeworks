from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
import os
from form import RegisterForm
from model import db, User
import hashlib

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.secret_key = "qweasdzxcqweasdzxc123@#!#"
csrf = CSRFProtect(app)
md5_hash = hashlib.new('md5')
db.init_app(app)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


@app.get('/')
def index():
    return 'Hi!'


@app.get('/registration')
def register_get():
    form = RegisterForm()
    return render_template('index.html', form=form)


@app.post('/registeration')
def register_post():
    form = RegisterForm()
    if form.validate():
        user_login = request.form.get('name')
        user_age = request.form.get('age')
        user_gender = request.form.get('gender')
        user_email = request.form.get('email')
        user_password_not_hidden = request.form.get('password')
        user_password = hash_password(user_password_not_hidden)
        user = User(user_login=user_login, user_age=user_age, user_gender=user_gender, user_email=user_email, user_password=user_password)
        db.session.add(user)
        db.session.commit()
        return render_template('success.html')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

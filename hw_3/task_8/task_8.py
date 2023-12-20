from flask import Flask, render_template, request
from models import db, User
import hashlib

md5_hash = hashlib.new('md5')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.secret_key = "qweasdzxcqweasdzxc123@#!#"
db.init_app(app)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


@app.get('/')
def index_get():
    return render_template('index.html')

@app.get('/register/')
def register_get():
    return render_template('register.html')

@app.post('/register/')
def register_post():
    user_login = request.form.get('login')
    user_email = request.form.get('email')
    user_password_not_hidden = request.form.get('password_1')
    user_password = hash_password(user_password_not_hidden)
    user = User(user_login=user_login, user_email=user_email, user_password=user_password)
    db.session.add(user)
    db.session.commit()
    return render_template('success.html')

@app.get('/success')
def success_get():
    return render_template('success.html')

@app.post('/success')
def success_post():
    return render_template('index.html')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

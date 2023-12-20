from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    user_age = db.Column(db.String(50), nullable=False)
    user_gender = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f'User({self.user_name}, {self.user_age}, {self.user_gender}, {self.user_email}, {self.user_password})'

from app import db, login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50))
    password_hashed = db.Column(db.String(200))

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
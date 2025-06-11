from app import db, login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50))
    password_hashed = db.Column(db.String(200))
    statement = db.relationship('Statement', backref='owner', lazy=True)
    

class Statement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(20))
    transaction_date = db.Column(db.Date)
    description_one = db.Column(db.String(200))
    description_two = db.Column(db.String(200))
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
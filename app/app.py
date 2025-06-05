from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '2NbF7oNgA57XNgiZ6NOcpN62PjlQWMbj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'

db = SQLAlchemy(app)


from app import routes
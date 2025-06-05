from app import app, db
from flask import render_template, flash, url_for, redirect
from app.forms import LoginForm, SignupForm

@app.route("/")

@app.route("/index", methods=["GET", "POST"])
def index():
    word = 'hello, world'

    return render_template("index.html", word=word, title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        return render_template("login.html", title="Login")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    sform = SignupForm()

    if sform.validate_on_submit():
        return render_template("signup.html", title="Sign-up")
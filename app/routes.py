from app import app, db
from flask import render_template, flash, url_for, redirect
from app.forms import LoginForm, SignupForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")

@app.route("/index", methods=["GET", "POST"])
def index():
    word = 'hello, world'

    return render_template("index.html", word=word, title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and check_password_hash(user.password_hashed, form.password.data):

            flash("user has logged in")
            return redirect(url_for("index"))
        else:
            flash("invalid credentials or user does not exist")
            return redirect(url_for("login"))
    return render_template("login.html", title="Login", form=form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    sform = SignupForm()

    if sform.validate_on_submit():
        user = User.query.filter_by(username=sform.username.data).first()
        if user:
            flash("user already exists!")
            return redirect(url_for("login"))
        else:
            hashed_password = generate_password_hash(sform.password.data)
            new_user = User(
                username=sform.username.data, 
                password=sform.password.data,
                password_hashed=hashed_password )

            db.session.add(new_user)
            db.session.commit()

            flash("user has been added to the database")
            return redirect(url_for("login"))
    return render_template("signup.html", title="Sign-up", sform=sform)
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
        flash("user has logged in")
        return redirect(url_for("index"))
    return render_template("login.html", title="Login", form=form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    sform = SignupForm()

    if sform.validate_on_submit():
        flash("user has been added to the database")
        return redirect(url_for("login"))
    return render_template("signup.html", title="Sign-up", sform=sform)
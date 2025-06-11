from app import app, db
from flask import render_template, flash, url_for, redirect
from app.forms import LoginForm, SignupForm, UploadForm
from app.models import User, Statement
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import pandas as pd
from werkzeug.utils import secure_filename
import os


@app.route("/", methods=["GET", "POST"])

@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    form = UploadForm()
    dataframe = None
    if form.validate_on_submit():
        df = pd.read_csv(form.file.data)
        dataframe = df.to_html()

        file = form.file.data
        secured_file = secure_filename(file.filename)

        path = os.path.join(app.config['UPLOAD_FOLDER'], secured_file)
        file.save(path)
        return render_template("index.html", dataframe=dataframe, form=form,  title="Home")
    
    return render_template("index.html", dataframe=dataframe, form=form,  title="Home")

@app.route("/add_csv", methods=["GET", "POST"])
def add_csv():

    return redirect(url_for("index"))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and check_password_hash(user.password_hashed, form.password.data):
            login_user(user)
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

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
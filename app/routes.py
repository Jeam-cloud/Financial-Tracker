from app import app, db
from flask import render_template, flash, url_for, redirect, request
from app.forms import LoginForm, SignupForm, UploadForm
from app.models import User, Statement
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import pandas as pd
from werkzeug.utils import secure_filename
import os, glob, datetime

@app.route("/", methods=["GET", "POST"])

@app.route("/landing", methods=["GET", "POST"])
def landing():
    return render_template("landing.html", title="Home")

@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    form = UploadForm()
    df = None

    if form.validate_on_submit():
        file = form.file.data
        secured_file = secure_filename(file.filename)

        path = os.path.join(app.config["UPLOAD_FOLDER"], secured_file)
        file.save(path)

        df = pd.read_csv(path).to_html()

    query = Statement.query.filter_by(user_id=current_user.id)

    selected_type = request.args.get("type", "All")

    if selected_type != "All":
        query = query.filter_by(account_type=selected_type)
    
    sort_type =request.args.get("sort")

    if sort_type == "highest":
        query = query.order_by(Statement.amount.desc())
    elif sort_type == "lowest":
        query = query.order_by(Statement.amount)

    rows = query.all()

    income, expenses = 0, 0
    for row in rows:
        if row.amount > 0:
            income += row.amount
        elif row.amount < 0:
            expenses += row.amount
    
    return render_template("index.html", title="Home", form=form, df=df, rows=rows, income=income, expenses=expenses)

@app.route("/add_csv", methods=["GET", "POST"])
@login_required
def add_csv():
    files = glob.glob(os.path.join(app.config["UPLOAD_FOLDER"], "*"))

    if files:
        latest_file = max(files, key=os.path.getmtime)
        flash("file found")

        df = pd.read_csv(latest_file, index_col=False)

        try:
            for _, row in df.iterrows():
                date = list(map(int, row["Transaction Date"].split("/")))

                rows = Statement(
                    account_type = row["Account Type"],
                    transaction_date = datetime.datetime(date[2], date[0], date[1]),
                    description_one = row["Description 1"],
                    description_two = row["Description 2"],
                    amount = row["CAD$"],
                    user_id = current_user.id
                )
                db.session.add(rows)
        except:
            flash("not an RBC CSV file")
        finally:
            os.remove(latest_file)
    
        db.session.commit()
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
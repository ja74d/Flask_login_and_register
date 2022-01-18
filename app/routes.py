from flask import render_template, redirect
from app import app, db
from app.forms import RegisterForm
from app.models import User
from werkzeug.security import generate_password_hash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)


#register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    user = User.query.filter_by(username=form.username.data).first()
    if form.validate_on_submit():
        if user is None:
            hash_pw = generate_password_hash(form.password.data, method='sha256')
            user = User(username=form.username.data, email=form.email.data, password_hash=hash_pw)
            db.session.add(user)
            db.session.commit()
            return redirect("/login")

    return render_template('register.html', form=form, title='Register')

#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login')

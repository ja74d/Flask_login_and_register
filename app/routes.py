from flask import render_template, redirect, flash, url_for
from app import app, db
from app.forms import RegisterForm, LoginForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required, LoginManager


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)


# register
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


# login page

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('dashboard'))
    return render_template('login.html', title='Login', form=form)


# create dashboard page
@app.route('/dashboard')
@login_required
def dashboard():
    title = 'Dashboard'
    return render_template('dashboard.html', title=title)

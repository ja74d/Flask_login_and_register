from flask import render_template, redirect, flash, url_for
from app import app, db
from app.forms import RegisterForm, LoginForm, PostForm
from app.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required, LoginManager


@app.route('/')
def index():
    title = 'Home'
    posts = Post.query.all()
    return render_template('index.html', title=title, posts=posts)


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


# logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        i_post = Post(title=form.title.data, author=current_user.username, content=form.content.data)
        db.session.add(i_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post.html', title='New Post', form=form)


# see post
@app.route('/post/<int:post_id>')
def see_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('see_post.html', titel='post', post=post)


# edit user
@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = RegisterForm()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password_hash = generate_password_hash(form.password.data, method='sha256')
        username = form.username.data
        db.session.commit()
        return redirect(url_for('dashboard'))
    else:
        form.username.data = user.username
        form.email.data = user.email
        form.password.data = user.password_hash
        form.password_confirm.data = user.password_hash
    return render_template('edit_user.html', title='Edit User', form=form, user=user)


# delete post
@app.route('/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.username == post.author:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('index'))
    elif current_user.username == "admin":
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        flash('You are not the author of this post.')
        return redirect(url_for('see_post', post_id=post_id))


# delete user
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if current_user.username == user.username:
        db.session.delete(user)
        db.session.commit()
        flash('good bye')
        return redirect(url_for('index'))
    else:
        flash("you cannot do that!")
        return redirect(url_for('index'))



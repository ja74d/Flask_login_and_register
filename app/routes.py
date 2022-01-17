from flask import render_template
from app import app
from app.forms import MyForm


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)


#register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = MyForm()
    return render_template('register.html', form=form)

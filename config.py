import os


# secret key for wtf forms
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'
    # + os.path.join(os.path.dirname(__file__), 'app.db')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://javad:********@localhost/blog_db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ''

import os


# secret key for wtf forms
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'
    # + os.path.join(os.path.dirname(__file__), 'app.db')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://javad:40517780@localhost/blog_db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://kriteofvhxekvf:dcdff79cffbfcac330d01a774899e310ab135bbb154d8444b20168107c7db252@ec2-34-230-110-100.compute-1.amazonaws.com:5432/dfrngetsr3n9lo'

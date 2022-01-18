from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

db = SQLAlchemy(app)




app.config.from_object(Config)

from app import routes

from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

api = Api()

db = SQLAlchemy(app)
ma = Marshmallow()
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models

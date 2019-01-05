from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

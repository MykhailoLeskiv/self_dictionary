from flask import Flask, Blueprint
from flask_admin import Admin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from app.config import Config

# initializing app
app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

# registering blueprint
myblueprint = Blueprint(name='self_dictionary',
                        import_name=__name__,
                        static_folder='static',
                        template_folder='templates',
                        static_url_path='/static',
                        url_prefix='/self_dictionary',
                        subdomain=None,
                        url_defaults=None,
                        root_path=None)
app.register_blueprint(myblueprint)

# initializing API
api = Api()
ma = Marshmallow()

# initializong admin view
admin = Admin(app, name='self_dictionary', template_mode='bootstrap3')

# initializing database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# initializing login view
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models

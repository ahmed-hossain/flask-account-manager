from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize all the flask extention
#login = LoginManager()
#login.login_view = 'auth.login'
db = SQLAlchemy()
migrate = Migrate()


# Create the app
app = Flask(__name__)
app.config.from_object(Config)


# Register the app to the extentions
#login.init_app(app)
db.init_app(app)
migrate.init_app(app)



# Register all the blueprints

from root.main import bp as main_bp
app.register_blueprint(main_bp)

from root.auth import  bp as auth_bp
app.register_blueprint(auth_bp)


# Moved to bottom to avoid circular import
from root import models
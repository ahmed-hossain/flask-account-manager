from flask import Flask

app = Flask(__name__)


# Register all the blueprints
# =============================

# Home page related stuff
from root.main import bp as main_bp
app.register_blueprint(main_bp)


# Authentication related stuff
from root.auth import  bp as auth_bp
app.register_blueprint(auth_bp)


# Moved to bottom to avoid circular import

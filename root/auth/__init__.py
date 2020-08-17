from flask import Blueprint

bp = Blueprint('auth', __name__)

from root.auth import routes
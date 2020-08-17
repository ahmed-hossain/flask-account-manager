from flask import Blueprint

bp = Blueprint('main', __name__)

from root.main import routes
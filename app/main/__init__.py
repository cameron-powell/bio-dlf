from flask import Blueprint


main = Blueprint('main', __name__)
from . import views, errors  # This is placed here intentionally to avoid circular dependencies.

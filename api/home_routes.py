from flask import Blueprint

api_routes_bp = Blueprint('home_api', __name__)


@api_routes_bp.route('/welcome')
def home():
    return 'Welcome to Gimmicks Travels - Python Flask API!'

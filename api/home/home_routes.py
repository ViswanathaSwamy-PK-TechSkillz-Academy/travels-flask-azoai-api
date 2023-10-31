from flask import Blueprint

home_api_bp = Blueprint('home_api_bp', __name__)


@home_api_bp.route('/home', methods=['GET'])
def home():
    return 'Welcome to Gimmicks Travels - Python Flask API!'

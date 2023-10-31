from flask import Blueprint

# Create a blueprint named 'home_api_bp'
home_api_bp = Blueprint('home_api_bp', __name__)

# Define a route for the blueprint


@home_api_bp.route('/home', methods=['GET'])
def home():
    return 'Welcome to Gimmicks Travels - Python Flask API!'

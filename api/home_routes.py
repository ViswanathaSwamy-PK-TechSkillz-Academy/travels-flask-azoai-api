from flask import Blueprint, current_app

home_api_bp = Blueprint('home_api_bp', __name__)

# Define a route for the blueprint


# Routes: http://127.0.0.1:5000 OR http://127.0.0.1:5000/api
@home_api_bp.route('/', methods=['GET'])
def home():
    current_app.logger.info("Processing request to home route")

    return 'Welcome to Gimmicks Travels - Python Flask API!'

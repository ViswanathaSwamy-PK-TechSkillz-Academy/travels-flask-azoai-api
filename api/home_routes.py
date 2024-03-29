from flask import Blueprint, current_app, jsonify

home_api_bp = Blueprint('home_api_bp', __name__)

# Define a route for the blueprint


# Routes: http://127.0.0.1:5009 OR http://127.0.0.1:5009/api
@home_api_bp.route('/', methods=['GET'])
def home():
    current_app.logger.info("Processing request to home route")

    # Simulate an error by raising an exception
    # raise Exception("This is a simulated error")

    return jsonify({'data': 'Welcome to Gimmicks Travels - Python Flask API!'}), 200

# Define an error handler for the custom exception


# @home_api_bp.errorhandler(Exception)
# def handle_custom_error(e):
#     response = jsonify({'error': str(e)})
#     response.status_code = 500  # You can set the appropriate status code
#     return response

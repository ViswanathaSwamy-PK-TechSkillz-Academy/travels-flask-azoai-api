from flask import Flask
from dotenv import dotenv_values

# Import the home.py route
from api.home.home_routes import home_api_bp

app = Flask(__name__)


def create_app():

    # Register the API routes blueprint
    app.register_blueprint(home_api_bp, url_prefix='/api')

    return app


# # mCreate the app and run it during development
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)  # During development

# # For production deployment, comment out the above lines and use the one below
# app = create_app()
# app.run()  # In production

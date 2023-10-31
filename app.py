from flask import Flask

from api.home_routes import home_api_bp
from api.azoai_routes import azoai_api_bp
from utils.logging_config import configure_logging

app = Flask(__name__)


def create_app():

    # Configure the app's logging settings
    configure_logging(app)

    app.logger.info("Starting Gimmicks Travels API")

    # Register the home_api_bp blueprint
    app.register_blueprint(home_api_bp, name='home_route_direct')
    app.register_blueprint(home_api_bp, url_prefix='/api')

    app.register_blueprint(azoai_api_bp, url_prefix='/api')

    return app


# # Create the app and run it during development (.\app.py)
# if __name__ == "__main__":
#     print("Starting Python Flask Server For Gimmicks Travels API")
#     app = create_app()
#     app.run(host='0.0.0.0', port=5000, debug=True)  # During development

# # For production deployment, comment out the above lines and use the one below (Flask run)
# print("Starting Python Flask Server For Gimmicks Travels API using Flask run")
app = create_app()
# app.run()  # In production

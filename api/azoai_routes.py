from flask import Blueprint, request, jsonify
from utils.GetCountryInfoFromAzureOpenAI import GetCountryInfoFromAzureOpenAI

azoai_api_bp = Blueprint('api_routes', __name__)

# Create an instance of the GetCountryInfoFromAzureOpenAI class
openai_helper = GetCountryInfoFromAzureOpenAI()

# Define the route to insert country information


@azoai_api_bp.route('/getcountryinfo', methods=['GET'])
def insert_country_info():
    try:
        # Parse the JSON data from the request
        country_data = request.get_json()

        # Get the country information from Azure OpenAI
        country_name = country_data.get('country_name')
        country_data = openai_helper.get_country_info(country_name)

        return jsonify(country_data), 200

    except Exception as e:
        azoai_api_bp.logger.exception(
            "An error occurred while processing the request:")

        return jsonify({'error': 'An error occurred while processing the request.'}), 500

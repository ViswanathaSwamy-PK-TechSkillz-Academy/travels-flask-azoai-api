from flask import Blueprint, request, jsonify
from utils.GetCountryInfoFromAzureOpenAI import GetCountryInfoFromAzureOpenAI

azoai_api_bp = Blueprint('azoai_api_bp', __name__)

# Create an instance of the GetCountryInfoFromAzureOpenAI class
openai_helper = GetCountryInfoFromAzureOpenAI()

# Define the route to insert country information


@azoai_api_bp.route('/getcountryinfo', methods=['GET'])
def insert_country_info():
    try:
        # Get the 'country_name' parameter from the query string
        country_name = request.args.get('country_name')

        if country_name is None:
            return "Missing 'country_name' parameter in the query string", 400

        # Get the country information from Azure OpenAI
        country_data = openai_helper.get_country_info(country_name)
        print(country_data)

        return [], 200

    except Exception as e:
        # azoai_api_bp.logger.exception(
        #     "An error occurred while processing the request:")
        print(e)
        return jsonify({'error': 'An error occurred while processing the request.'}), 500

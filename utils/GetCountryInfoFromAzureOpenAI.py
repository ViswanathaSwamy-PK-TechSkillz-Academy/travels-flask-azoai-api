import json
from openai import AzureOpenAI
import os
from utils.env_config import get_config_value


class GetCountryInfoFromAzureOpenAI:
    client = None

    def __init__(self):
        print(os.getenv("OPENAI_API_KEY"))
        client = AzureOpenAI(
            api_version=get_config_value('OPENAI_API_VERSION'),
            azure_endpoint=get_config_value('OPENAI_API_BASE'),
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        self.client = client

    def get_country_info(self, country_name):
        input_prompt = f"Please give me the country_name, capital_state, national_bird, country_population for {
            country_name} in flat JSON object. country_population should be in BIGINT without separators"

        response = self.client.completions.create(
            model=get_config_value(
                'COMPLETIONS_MODEL_DEPLOYMENT_NAME'),
            prompt=input_prompt,
            temperature=1,
            max_tokens=300,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=None)

        # print(response)

        # Assuming the response.choices[0].text is a JSON string
        country_info_json = response.choices[0].text

        # Convert the JSON string to a dictionary
        country_info = json.loads(country_info_json)

        return country_info

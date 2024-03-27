# dalle_integration.py

from openai import AzureOpenAI
from utils.env_config import get_config_value
import json
import os


class DALLEIntegration:
    def __init__(self):
        self.client = AzureOpenAI(
            api_version=get_config_value["OPENAI_API_VERSION"],
            azure_deployment=get_config_value["OPENAI_API_DEPLOYMENT"],
            azure_endpoint=get_config_value["OPENAI_API_ENDPOINT"],
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def generate_image(self, prompt, size="1024x1024", n=1):
        try:
            result = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                n=n
            )

            image_url = json.loads(result.model_dump_json())['data'][0]['url']
            return image_url

        except Exception as e:
            print(f"An error occurred: {e}")
            return None


import requests
import os

def save_image_locally(image_url, local_path):
    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the file name from the URL
            file_name = os.path.basename(image_url)

            # Save the image to the specified local path
            with open(os.path.join(local_path, file_name), 'wb') as f:
                f.write(response.content)
            
            print(f"Image saved successfully to: {local_path}/{file_name}")
            return True
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return False

    except Exception as e:
        print(f"An error occurred while saving the image: {e}")
        return False

# Example usage
image_url = "https://dalleproduse.blob.core.windows.net/private/images/658d2694-13de-4c7f-bafa-fe5468a1944c/generated_00.png?se=2024-03-27T17%3A15%3A13Z&sig=vizQi0XwS1ZhbybGkfE%2BhXQvj2Jo3vU4WkRoNs91ODM%3D&ske=2024-04-02T12%3A41%3A47Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2024-03-26T12%3A41%3A47Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02"
local_path = "path/to/save/image"

# Call the function to save the image locally
save_image_locally(image_url, local_path)

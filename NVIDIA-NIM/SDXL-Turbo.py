import os
from dotenv import load_dotenv
load_dotenv()
nvidia_api_key = os.getenv('SDXL_API_KEY')
import requests

invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/sdxl-turbo"

headers = {
    "Authorization": f"Bearer {nvidia_api_key}",
    "Accept": "application/json",
}

payload = {
    "text_prompts": [{"text": "A steampunk dragon soaring over a Victorian cityscape, with gears and smoke billowing from its wings."}],
    "seed": 0,
    "sampler": "K_EULER_ANCESTRAL",
    "steps": 2
}

response = requests.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
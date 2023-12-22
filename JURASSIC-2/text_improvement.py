import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')
# API KEY
api_key = os.getenv('API_KEY')

if api_key is None:
    print("API no se encontro en el .env file como 'API_KEY=YOUR_API_KEY'")
    exit()

# API endpoint
url = "https://api.ai21.com/studio/v1/improvements"

# Request
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Request payload (if needed, add payload data)
data = {
    "types": ["fluency", "vocabulary/specificity"], # Hay mas: , "vocabulary/variety", "clarity/short-sentences", "clarity/conciseness"
    'text': input("Texto a mejorar: ") # e.g   Whatsup men you are good to go now
}

# POST
response = requests.post(url, headers=headers, json=data)

# response
if response.status_code == 200:
    print('Request successful!')
    print('Response:', response.json())
else:
    print('Request failed with status code:', response.status_code)
    print('Response:', response.text)

import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')
api_key = os.getenv('API_KEY')
# API 
url = 'https://api.ai21.com/studio/v1/paraphrase'
headers = {
    'Authorization': f'Bearer {api_key}',
    'accept': 'application/json',
    'content-type': 'application/json'
}
"""
Tipos de estilos
General - there are fresh and creative ways to rephrase sentences. Offer them to your users.
Casual - convey a friendlier and more accessible tone for the right audience.
Formal - present your words in a more professional way.
Short - express your messages clearly and concisely.
Long - expand your sentences to give more detail, nuance and depth.
"""
data = {
    'style': 'formal', # Hay diversos estilos 
    'text': input('Texto a resumir: ') # e.g  Hi I was wondering if you can help with my order please 
}

# POST
response = requests.post(url, headers=headers, json=data)

# Obtener response
if response.status_code == 200:
    print('Request successful!')
    print('Response:', response.json())
else:
    print('Request failed with status code:', response.status_code)
    print('Response:', response.text)

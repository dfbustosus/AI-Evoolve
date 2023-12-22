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
url = "https://api.ai21.com/studio/v1/summarize"

# Request
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Request payload (if needed, add payload data)
data = {
    "sourceType": "TEXT", # Hay mas: , "vocabulary/variety", "clarity/short-sentences", "clarity/conciseness"
    'source': input("Texto a resumir: ") # e.g  The Industrial Revolution was a pivotal time in history that saw the transition from hand production methods to machine-based manufacturing. It began in the late 18th century in Britain and later spread to other parts of the world, fundamentally changing society, economics, and culture. The introduction of new machinery and technology led to increased productivity, urbanization, and significant shifts in employment patterns. This period brought about advancements in transportation, communication, and the growth of industries such as textiles, iron, and coal mining. The Industrial Revolution laid the groundwork for modern manufacturing processes and played a crucial role in shaping the world as we know it today.
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

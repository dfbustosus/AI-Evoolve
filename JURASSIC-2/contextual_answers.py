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
url = "https://api.ai21.com/studio/v1/answer"

# Request
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# data
data= {
    "context": "The advent of quantum computing has sparked immense interest and innovation across various industries. Quantum computers leverage quantum mechanics to perform computations that surpass the capabilities of classical computers. Their ability to handle complex algorithms and solve certain problems exponentially faster than classical computers presents significant opportunities in fields like cryptography, drug discovery, optimization, and machine learning. Despite the potential quantum computing holds, the technology is still in its early stages, facing challenges such as error correction, scalability, and maintaining quantum coherence. Researchers and tech companies worldwide are racing to overcome these obstacles and unlock the full potential of quantum computing.",
    "question": input("Pregunta: ") # e.g What are some challenges faced by quantum computing despite its potential?
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

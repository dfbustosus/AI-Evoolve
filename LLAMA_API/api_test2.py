import json
import os
from dotenv import load_dotenv
from llamaapi import LlamaAPI  # Replace with your actual module or API

load_dotenv('.env')

api_key = os.getenv('API_KEY')
llama = LlamaAPI(api_key)

# Request
api_request_json = {
    "messages": [
        {"role": "user", "content": "What is the capital of France?"}
    ],
    "functions": [
        {
            "name": "get_country_info",
            "description": "Get information about a country",
            "parameters": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                        "description": "Name of the country"
                    }
                }
            },
            "required": ["country"]
        }
    ],
    "stream": False,
    "function_call": "get_country_info"
}

# Request
response = llama.run(api_request_json)

# Impromir el JSON
print(json.dumps(response.json(), indent=2))

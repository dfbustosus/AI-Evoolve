#! pip install llamaapi
import json
import os
from dotenv import load_dotenv
load_dotenv('.env')
api_key = os.getenv('API_KEY')
from llamaapi import LlamaAPI

# Inicializar el SDK
llama = LlamaAPI(api_key)

# API request
api_request_json = {
    "messages": [
        {"role": "user", "content": "What is the weather like in Boston?"},
    ],
    "functions": [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "days": {
                        "type": "number",
                        "description": "for how many days ahead you wants the forecast",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
            },
            "required": ["location", "days"],
        }
    ],
    "stream": False,
    "function_call": "get_current_weather",
}

# Ejecutar el request
response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))
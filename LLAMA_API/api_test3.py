import json
import os
from dotenv import load_dotenv
from llamaapi import LlamaAPI  #

load_dotenv('.env')

api_key = os.getenv('API_KEY')

llama = LlamaAPI(api_key)

api_request_json = {
    "messages": [
        {"role": "user", "content": "Please solve the equation: 3x^2 + 2x - 7 = 0"}
    ],
    "functions": [
        {
            "name": "solve_equation",
            "description": "Solve a quadratic equation",
            "parameters": {
                "type": "object",
                "properties": {
                    "equation": {
                        "type": "string",
                        "description": "Quadratic equation to be solved"
                    }
                }
            },
            "required": ["equation"]
        }
    ],
    "stream": False,
    "function_call": "solve_equation"
}

# Request
response = llama.run(api_request_json)

# Response
print(json.dumps(response.json(), indent=2))

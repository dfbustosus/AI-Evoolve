import json
import os
from dotenv import load_dotenv
from llamaapi import LlamaAPI  

load_dotenv('.env')

api_key = os.getenv('API_KEY')

llama = LlamaAPI(api_key)

api_request_json = {
    "messages": [
        {
            "role": "user",
            "content": "Can you calculate the compound interest for an investment of 3000 USD in 5 years with a monthly annual rate of 5 percent?"
        }
    ],
    "functions": [
        {
            "name": "calculate_compound_interest",
            "description": "Calculate compound interest for an investment",
            "parameters": {
                "type": "object",
                "properties": {
                    "principal": {
                        "type": "number",
                        "description": "Initial investment amount"
                    },
                    "rate": {
                        "type": "number",
                        "description": "Annual interest rate (as a decimal)"
                    },
                    "time": {
                        "type": "number",
                        "description": "Time period (in years)"
                    },
                    "compounds_per_year": {
                        "type": "number",
                        "description": "Number of times the interest is compounded per year"
                    }
                }
            },
            "required": ["principal", "rate", "time", "compounds_per_year"]
        }
    ],
    "stream": False,
    "function_call": "calculate_compound_interest"
}

# Execute the request
response = llama.run(api_request_json)

# Print the response (JSON format)
print(json.dumps(response.json(), indent=2))

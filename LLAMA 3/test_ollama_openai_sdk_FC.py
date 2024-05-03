import requests
import json
import sys 

schema= {
    "location": {
        "type":"string",
        "description": "The city and state, e.g. San Francisco, CA"
    },
    "format":{
        "type":"string",
        "description": "The temperature unit to use. Infer this from the users location. e.g C or F"
    }
}

#print(json.dumps(schema))

payload ={
    "model": "llama3",
    "messages":[
        {"role":"assistant","content": f"You are a helpful AI Assistant. You must extract the location and the format from the following messages. Output must be in JSON always using the schema defined here: {json.dumps(schema)}"},
        {"role": "user","content": "The actual weather in San Diego is 34 celsius degree"},
    ],
    "format":"json",
    "stream":False,
    "options": {
    "seed": 123,
    "temperature": 0.01
  }
}

response= requests.post(
    "http://localhost:11434/api/chat",
    json= payload
)

print(response.json())
import requests
import json
import sys 

payload ={
    "model": "llama3",
    "messages":[
        {"role":"assistant","content": "Eres un asistente que tiene mas de 30 años de experiencia en call centers. Ayuda de la mejor forma al cliente para que pueda agendar una cita medica"},
        {"role":"user","content": "Hola buen dia quisiera agendar una cita medica"},
    ],
    "format":"json",
    "stream":False, # True
    "options": {
        #"seed": 123,
        "temperature": 0.7
  }
}

response= requests.post(
    "http://localhost:11434/api/chat",
    json= payload
)

print(response.json())

print('-------------------------------------')
#print(response.json()['message']['content'].)
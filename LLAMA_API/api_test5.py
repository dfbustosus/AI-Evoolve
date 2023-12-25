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
            "content": "¿Puedes calcular el interés compuesto para una inversión de 3000 USD durante 5 años con una tasa anual del 5 por ciento, capitalizada mensualmente?"
        }
    ],
    "functions": [
        {
            "name": "calcular_interes_compuesto",
            "description": "Calcular el interés compuesto para una inversión",
            "parameters": {
                "type": "object",
                "properties": {
                    "principal": {
                        "type": "number",
                        "description": "Monto inicial de la inversión"
                    },
                    "tasa": {
                        "type": "number",
                        "description": "Tasa de interés anual (en decimal)"
                    },
                    "tiempo": {
                        "type": "number",
                        "description": "Período de tiempo (en años)"
                    },
                    "compuestos_por_anio": {
                        "type": "number",
                        "description": "Número de veces que se capitaliza el interés por año"
                    }
                }
            },
            "required": ["principal", "tasa", "tiempo", "compuestos_por_anio"]
        }
    ],
    "stream": False,
    "function_call": "calcular_interes_compuesto",
}

# Request
response = llama.run(api_request_json)

# Response
print(json.dumps(response.json(), indent=2))

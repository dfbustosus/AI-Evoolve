# 0. Dependencias
import requests
from dotenv import load_dotenv
import os
load_dotenv()
url_base = os.environ.get("API_URL")
# 1. Definimos el prompt
RAVEN_PROMPT = \
'''
Function:
def get_weather_data(coordinates):
    """
    Fetches weather data from the Open-Meteo API for the given latitude and longitude.

    Args:
    coordinates (tuple): The latitude of the location.

    Returns:
    float: The current temperature in the coordinates you've asked for
    """

Function:
def get_coordinates_from_city(city_name):
    """
    Fetches the latitude and longitude of a given city name using the Maps.co Geocoding API.

    Args:
    city_name (str): The name of the city.

    Returns:
    tuple: The latitude and longitude of the city.
    """

User Query: {query}<human_end>
'''
# 2. Define tu pregunta
#QUESTION = "Whats's the weather like in Seattle right now?"
QUESTION = input("Ingresa tu pregunta aquí: ")
# 3. Definir la URL del endpoint
API_URL = url_base
headers = {
        "Content-Type": "application/json"
}

# 4. Definir funcion para obtener la query
def query(payload):
	"""
	envia el payload al TGI endpoint.
	"""
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
# 5. Definir funcion raven query
def query_raven(prompt):
	"""
	Esta funcion envia el request al enpoint de TGI endpoint para obtener las llamdadas de Raven's .
	Esto no genera una justificacion, esto lo hicieron para resolver la latencia
	"""
	output = query({
		"inputs": prompt,
		"parameters" : {"temperature" : 0.001, "stop" : ["<bot_end>"], "do_sample" : False, "max_new_tokens" : 2000}})
	call = output[0]["generated_text"].replace("Call:", "").strip()
	return call
# 6. Funcion de razonamiento
def query_raven_with_reasoning(prompt):
	"""
	Envia un request al TGI endpoint para obtener el function call Y la justificacion de la llamada
	"""
	output = query({
		"inputs": prompt,
		"parameters" : {"temperature" : 0.001, "do_sample" : False, "max_new_tokens" : 2000}})
	call = output[0]["generated_text"].replace("Call:", "").strip()
	return call
# 7. Enviar el resultado
my_question = RAVEN_PROMPT.format(query = QUESTION)
raven_call = query_raven(my_question)
print('--------------------------------------')
print (f"LLamada de Raven \n: {raven_call}")

# 8. Explorar el resultado de razonamiento
my_question = RAVEN_PROMPT.format(query = QUESTION)
raven_call = query_raven_with_reasoning(my_question)
print('--------------------------------------')
print (f"Explicacion de la llamada \n: {raven_call}")

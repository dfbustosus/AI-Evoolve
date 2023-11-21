###################################################
# 1. Librerias
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv
import requests
import os
###################################################
# 2. Cargar variables entorno
load_dotenv()
openai_key = os.getenv("OPENAI_KEY")
#print(openai_key)
###################################################
# 3. Crear el asistente
client= OpenAI(api_key= openai_key)

input_user = input('Ingresa el prompt: ')

response = client.images.generate(
  model="dall-e-3",
  prompt=input_user,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print("Image URL:", image_url)

# Guardar la imagen en un folder especifico
folder_path = "./images/generation/"
if not os.path.exists(folder_path): os.makedirs(folder_path)

with open(f'./images/generation/Imagen_{input_user}.txt', 'w') as file:
    # Write the text into the file
    file.write(image_url)
## Prompts
"""
1. A Pickachu in paris
2. Un soldado en una batalla
3. Lebron james encestando
4. A person coding a complex problem
"""
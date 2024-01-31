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
  quality="hd", # standard, hd
  n=1,
)

image_url = response.data[0].url
print("Image URL:", image_url)

# Guardar la imagen en un folder especifico
folder_path = "./images/generation/"
if not os.path.exists(folder_path): os.makedirs(folder_path)

#with open(f'./images/generation/Imagen_{input_user}.txt', 'w') as file:
with open(f'./images/generation/Imagen_a.txt', 'w') as file:
    # Write the text into the file
    file.write(image_url)
## Prompts
"""
1. A Pickachu in paris
2. Un soldado en una batalla
3. Lebron james encestando
4. A person coding a complex problem
5. Envision a vibrant cultural organization meeting at Kenility, a leading IT software company. Picture a grand conference room adorned with the invigorating hues of aquamarine, the signature color of the Kenility brand. In this inspiring setting, diverse employees from various cultural backgrounds come together for a collaborative brainstorming session. Capture the essence of unity and creativity as team members share their unique perspectives, fostering an inclusive atmosphere where every voice is valued. Emphasize the positive energy and enthusiasm as the Kenility team collaborates to generate innovative ideas. Ensure that the depiction avoids any negative feelings or inappropriate behaviors, maintaining a focus on the company's commitment to a supportive and respectful work culture
"""
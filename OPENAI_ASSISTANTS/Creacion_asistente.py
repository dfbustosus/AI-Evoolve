###################################################
# 1. Librerias
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv
import os
from Funciones import gather_user_data, gather_health_data, gather_appointment_data, not_talk
###################################################
# 2. Cargar variables entorno
load_dotenv()
openai_key = os.getenv("OPENAI_KEY")
#print(openai_key)
###################################################
# 3. Crear el asistente
client= OpenAI(api_key= openai_key)
###################################################
# 4. Crear el asistente
assistant = client.beta.assistants.create(
    name ="David Appointment Bot",
    instructions="No hagas supuestos acerca de los valores a utilizar en las funciones. Eres un aisstente que permite agendar una cita medica a un paciente. Pregunta primero por nombre, apellido, email y telefono. Posteriormente pregunta por la razon de la cita. Luego pregunta detalles de la cita: fecha y hora. Finalmente si el usuario no quiere hablar mas deberas terminar la conversacion.",
    model="gpt-4-1106-preview", # "gpt-4-1106-preview","gpt-3.5-turbo-1106"
    tools=[{"type": "function","function": gather_user_data},
           {"type": "function","function": gather_health_data},
           {"type": "function","function": gather_appointment_data},
           {"type": "function","function": not_talk}]
)

print(assistant.id) # Asistente creado
###################################################
# 5. Listar asistentes
mis_asistentes=client.beta.assistants.list(order="desc",limit="20")
pprint(mis_asistentes.data)

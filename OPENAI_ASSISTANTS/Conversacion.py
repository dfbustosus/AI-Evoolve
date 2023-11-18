###################################################
# 1. Librerias
from pprint import pprint
import json
from openai import OpenAI
import time
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
print(gather_appointment_data)
###################################################
# 4. Obtener el asistente creado el asistente
assistant= client.beta.assistants.retrieve("asst_1ytHgoX0Xn1kUNPIJTIeP1i1")
# 5. Conversacion
stop = True
# 5.1 crear un empty thread
thread= client.beta.threads.create()
while stop:
  # 5.2 Anadir un mensaje al asistente
  user_input = input('user: ')
  message = client.beta.threads.messages.create(thread_id=thread.id,role= "user",content= user_input)
  # 5.3 # Correr el asistente para obtener una respuesta
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id) # instructions="Algo adicional que quiero que haga"
  # 5.4 Obtener el estatus de la corrida 
  i=0
  while run.status not in ["completed","failed","requires_action"]:
    continue_asking= False
    if i>0: time.sleep(2)
    run= client.beta.threads.runs.retrieve(thread_id=thread.id,run_id = run.id)
    i+=1
    #print(run.status)
  # 5.5 Llamar al agente si status = "requires_action"
  if run.status == "requires_action":
      tools_to_calls = run.required_action.submit_tool_outputs.tool_calls
      #print(len(tools_to_calls),tools_to_calls)
      # 5.5.1 Ejecutar la accion dada
      tool_output_array=[]
      for each_tool in tools_to_calls:
        tool_call_id = each_tool.id
        function_name = each_tool.function.name
        function_arg= each_tool.function.arguments
        print("Tool Id: ", tool_call_id)
        print("Function to call: ", function_name)
        print("Parameters to use: ", function_arg)
        if function_name =="gather_user_data":
          ## Extraer datos de la funcion para hacer algo que quieras !!!!!!!!!
          telefono= json.loads(function_arg)['telefono'];nombre= json.loads(function_arg)['nombre'];
          apellido= json.loads(function_arg)['apellido'];email= json.loads(function_arg)['email'];
          print('Telefono: ', telefono, ' Nombre: ', nombre, ' Apellido: ', apellido, ' Email: ', email)
          output= "Ahora pregunta sobre el motivo de la consulta"
        elif function_name =="gather_health_data":
          output= "Ahora pregunta sobre detalles para la cita"
        elif function_name =="gather_appointment_data":
          output= "Informa al usuario que la cita ha sido agendada satisfactoriamente"
        elif function_name == "not_talk":
          if json.loads(function_arg)['fin'] == True: stop=False;
          output= "Genial que tengas un gran dia fue un gusto ayudarte hoy dia"
        tool_output_array.append({"tool_call_id": tool_call_id, "output": output})
      # 5.5.2 Return los resultados de cada run operation
      run = client.beta.threads.runs.submit_tool_outputs(thread_id=thread.id,run_id= run.id,tool_outputs=tool_output_array)
      # 5.5.3 ReChequear el status de nuevo
      i=0
      while run.status not in ["completed","failed","requires_action"]:
        if i>0:
          time.sleep(2)
        run= client.beta.threads.runs.retrieve(thread_id=thread.id,run_id = run.id)
        i+=1
  else:
      pass
  # 5.6 Obtener la data de la conversaicon
  messages=client.beta.threads.messages.list(thread_id=thread.id)
  reversed_messages = list(reversed(list(messages)))
  print('Asistente: ', reversed_messages[-1].content[0].text.value)
  # 3.7 Guardar la lista final de mensales
  if stop == False:
    list_messages = []
    for each in reversed_messages:
      list_messages.append({each.role: each.content[0].text.value})
    break
print("===================================")
print('Record de mensajes')
print(list_messages)
print("===================================")
# Llama 3 + Ollama + Service API

## Fase 1: Experimentando desde Ollama
1. Debes tener instalado Ollama, sino lo tienes solo debes descargar y seguir los pasos en este link: https://ollama.com/
2. Ahora puedes abrir una terminal y simplemente colocar los siguientes comandos
```bash
ollama run llam3
```
Si no tienes este modelo se descargará (pesa alrededor de 5GB) así que ten paciencia mientras descarga

3. Luego de esto simplemente podrás ejecutar el modelo ante cualquier prompt
```
Hola como estas hasta que fecha fuiste entrenado
```
4. Puedes ver la lista de modelos con :
```
ollama list
```
5. Si quieres remover cualquier modelo solo debes utilizar el comando 
```bash
ollama rm llama3
```
Por defecto el modelo llama3 es el `llama3:latest` de 7 Billones de parametros, para poder correrlo necesitaras alrededor de una gpu de 8GB (https://github.com/ollama/ollama/blob/main/docs/gpu.md), si quisieras correr el de 70 Billones de parametros sería necesario tener al menos 64GB de RAM. La versión que corre en tu computadora probablemente sea una versión quantizada
6. Otros comandos que puedes usar son:
```bash
/show info         Show details for this model
/show license      Show model license
/show modelfile    Show Modelfile for this model
/show parameters   Show parameters for this model
/show system       Show system message
/show template     Show prompt template
```
7. También puedes usar el comando `help` para obtener ayuda sobre el modelo
```bash
help
```

## Fase 2: Usando la API de Ollama 

1. Podremos usar las siguientes librerías y el script `test_ollama_api.py` para poder ejecutar el modelo desde una API. Recuerda que Ollama es como un servidor donde se pueden desplegar modelos

```python
payload ={
    "model": "llama3",
    "messages":[
        {"role":"assistant","content": f"You are a helpful AI Assistant. You must extract the phoneNumber and the appointmentReason from the following messages. Output must be in JSON always using the schema defined here: {json.dumps(schema)}"},
        {"role": "assistant","content": "Today is Friday 5 May 2024. The customer phone nomber is is 990901883."},
        {"role": "assistant","content": "Consider the leap years."},
        {"role": "assistant","content": "If the information provided by the customer sounds incomplete, repeat what you understood and ask for confirmation"},
        {"role": "assistant","content": "Always beautify the sentences and input field names for the customer."},
        {"role": "assistant","content": "If the user asks about address, please answer: 674 Straits Turnpike, Watertown, CT 06795. If the user asks about inspection stickers, please answer: Sadly we dont have inspection stickers at this moment. If the user asks about a car wash, please answer: Our dealership is happy to offer complimentary car wash for our customers"},
        {"role": "user","content": "Good morning. Well, and my vehicle needs a tire rotation."},
        {"role": "assistant","content": "Certainly, we can assist with an oil change for your vehicle. Could you please confirm if your phone number is 1345678906"},
        {"role": "user","content": "Well my phone number is 1565765134."},
        #{"role": "user","content": "Oh sorry actually my number is 1565765678."},
        {"role": "user","content": "Oh sorry actually my number is one five six five seven six five seven six eight"},
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
```

2. De la misma forma también puedes simpelmente abrir una terminal y enviar la petición (es mas rápido que usar un lenguaje de intermediario)

```bash
curl http://localhost:11434/api/chat -d '{
    "model": "llama3",
    "messages": [
        { "role": "system", "content": "You are a service agent to schedule medical appointments" },
        { "role": "user", "content": "I need to schedule an appointment please" }
    ],
    "stream":false
  }'
```

3. Este model también es capaz de lidiar con diversos flujos de conversaciones por ejemplo

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    },
    {
      "role": "assistant",
      "content": "due to rayleigh scattering."
    },
    {
      "role": "user",
      "content": "how is that different than mie scattering?"
    }
  ],
  "stream":false
}'
```

4. También es posible que definar diversos parametros de interés (REF: https://github.com/ollama/ollama/blob/main/docs/api.md)

```bash
curl http://localhost:11434/api/chat -d '{
    "model": "llama3",
    "messages": [
        { "role": "system", "content": "You are a mathematical professor to help students" },
        { "role": "user", "content": "I need help with my homework" }
    ],
    "stream":false,
    "options": {
        "num_keep": 5,
        "seed": 42,
        "num_predict": 100,
        "top_k": 20,
        "top_p": 0.9,
        "tfs_z": 0.5,
        "typical_p": 0.7,
        "repeat_last_n": 33,
        "temperature": 0.8,
        "repeat_penalty": 1.2,
        "presence_penalty": 1.5,
        "frequency_penalty": 1.0,
        "mirostat": 1,
        "mirostat_tau": 0.8,
        "mirostat_eta": 0.6,
        "penalize_newline": true,
        "stop": ["\n", "user:"],
        "numa": false,
        "num_ctx": 1024,
        "num_batch": 2,
        "num_gqa": 1,
        "num_gpu": 1,
        "main_gpu": 0,
        "low_vram": false,
        "f16_kv": true,
        "vocab_only": false,
        "use_mmap": true,
        "use_mlock": false,
        "rope_frequency_base": 1.1,
        "rope_frequency_scale": 0.8,
        "num_thread": 8
      }
  }'
```
## Fase 3: Usando la SDK de OpenAI

1. En este caso podemos usar el script `test_ollama_openai_sdk.py` para poder ver que incluso son el SDK de openAI podemos interactuar con nuestros modelos en Ollama

```python
from openai import OpenAI
client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)
chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'assistant','content':'You are a math professor with more than 30 years of experience in trigonomerty.'},
        {'role':'user','content': 'Can you tell me the basic idea behind Pythagoras theorem'},
        {'role':'assistant','content':"One of my favorite topics!\n\nThe fundamental idea behind Pythagoras' theorem is that for a right-angled triangle (where one angle is 90 degrees), the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.\n\nIn mathematical notation, this can be expressed as:\n\na^2 + b^2 = c^2\n\nwhere a and b are the lengths of the two sides that meet at the right angle (called legs), and c is the length of the hypotenuse. This equation holds true regardless of the sizes of the three sides.\n\nPythagoras' theorem has numerous applications in various fields, such as geometry, algebra, physics, engineering, and computer science. It's a fundamental tool for solving problems involving right triangles and is widely used in many areas of mathematics and science"},
        {'role':'user','content': 'Can you explain it in more simple terms please?'},
    ],
    model='llama3',
)
print(chat_completion.choices[0].message.content)
print('---------------------------------')
print('Created at: ',chat_completion.created)
print('Model: ',chat_completion.model)
print('Object: ',chat_completion.object)
print('Finger print: ',chat_completion.system_fingerprint)
print('Completion tokens',chat_completion.usage.completion_tokens)
print('Prompt tokens: ',chat_completion.usage.prompt_tokens)
print('Total tokens: ',chat_completion.usage.total_tokens)
```

2. Otra pregunta interesante que algunas personas se pueden hacer es si puedo utilizar function calling dentro de Ollama, la verdad es que si por ejemplo (`test_ollama_openai_sdk_FC.py`):

```python
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
```

Sin embargo ten presente que si usas un modelo simple probablemente no sea tan preciso como GPT, pero es una muy buena oportunidad para testear modelos open source

Fin!!
import requests
import json
url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama2",
    #"prompt": "What is a class in golang with an example"
    "prompt": "Hello how are you",
    "stream": False,
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
        "penalize_newline": True,
        #"stop": ["\n", "user:"],
        "numa": False,
        "num_ctx": 1024,
        "num_batch": 2,
        "num_gpu": 1,
        "main_gpu": 0,
        "low_vram": False,
        "f16_kv":True,
        "vocab_only": False,
        "use_mmap": True,
        "use_mlock": False,
        "num_thread": 8
  }
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

#print(response.json())
print(response.text)
print('-------------------------------')
print(json.dumps(response.json()))
print('-------------------------------')
print(json.dumps(response.json()['response']))
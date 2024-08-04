
import requests, base64
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
import requests, base64
nvidia_api_key = os.getenv('DEPLOT_API_KEY')

invoke_url = "https://ai.api.nvidia.com/v1/vlm/google/deplot"
stream = False# True

with open("economic-assistance-chart.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"

headers = {
  "Authorization": f"Bearer {nvidia_api_key}",
  "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
  "messages": [
    {
      "role": "user",
      "content": f'Generate underlying data table of the figure below: <img src="data:image/png;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 1024,
  "temperature": 0.20,
  "top_p": 0.20,
  "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())

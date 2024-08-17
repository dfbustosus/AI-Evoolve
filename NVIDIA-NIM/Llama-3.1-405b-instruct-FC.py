import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
nvidia_api_key = os.getenv('NVIDIA_API_KEY')

from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = nvidia_api_key
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-405b-instruct",
  messages=[
    #{"role":"system","content":"You are a customer service agent to help in weather"},
    {"role":"user","content":"The weather for San Francico will be 25 Celsius with a nice sky blue "}
    ],
  temperature=0.8,
  top_p=0.7,
  max_tokens=1024,
  stream=False,
  tools=[
    {
      "type":"function",
      "function":
        {
          "name":"get_current_weather",
          "description":"Returns the current weather at a location, if one is specified, and defaults to the user's location.",
          "parameters":{
            "type":"object",
            "properties":
                {
                  "location":
                    {
                      "type":"string",
                      "description":"The location to find the weather of, or if not provided, it's the default location."
                    },
                    "format":
                    {
                      "type":"string",
                      "enum":["celsius","fahrenheit"],
                      "description":"Whether to use SI or USCS units (celsius or fahrenheit)."
                    }
                },
            "required":[]
            }
        }
    }],
  tool_choice="auto"
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")


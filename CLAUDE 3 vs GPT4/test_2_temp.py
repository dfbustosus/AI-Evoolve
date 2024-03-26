# 1. Libraries
import anthropic
import ast
import re
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv
import json
from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt
from termcolor import colored  
import time

# 2. Env variables
GPT_MODEL = "gpt-3.5-turbo-0613"
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("CLAUDE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/complete"
ANTHROPIC_API_VERSION = "2023-06-01"

# 3. Instances 
anthropic_instance = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
openai_instance = OpenAI(api_key= OPENAI_API_KEY)

# 4. User input
user_input = "Tomorrow's forecast predicts a high of 25°C with clear skies"

# 5. Anthropic definition
STRING_ANTHROPIC = """
In this environment you have access to a set of tools you can use to answer the user's question.

You may call them like this:
<function_calls>
<invoke>
<tool_name>$TOOL_NAME</tool_name>
<parameters>
<$PARAMETER_NAME>$PARAMETER_VALUE</$PARAMETER_NAME>
...
</parameters>
</invoke>
</function_calls>

Here are the tools available:
<tools>
<tool_description>
<tool_name>get_temperature</tool_name>
<description>Gets the current temperature from a forecast sentence. Returns float: The forecast temperature. Raises ValueError: if the input temperature is invalid/unknown.
<parameters>
<parameter>
<name>temperature</name>
<type>string</type>
<description>The numerical value representing the thermal condition measured in degrees Celsius or Fahrenheit.</description>
</parameter>
</parameters>
</tool_description>
</tools>
"""

content_to_send = {"role": "user", "content": f"{STRING_ANTHROPIC}\n\nHuman:{user_input}\n\nAssistant:"}
conversation_logs=[]
conversation_logs.append(content_to_send)

start_time = time.time()

response = anthropic_instance.messages.create(
    max_tokens=1024,
    messages=conversation_logs,
    model="claude-3-opus-20240229",
)

end_time = time.time()

print("===========================================================================================================")
print("ANTHROPIC OUTPUT")

print(response.content[0].text)
elapsed_time = end_time - start_time

print('Time for output: ', elapsed_time)

# 6. Openai definition
@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, tools=None, tool_choice=None, model=GPT_MODEL):
    try:
        response = openai_instance.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue",
        "function": "magenta",
    }
    
    for message in messages:
        if message["role"] == "system":
            print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and message.get("function_call"):
            print(colored(f"assistant: {message['function_call']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and not message.get("function_call"):
            print(colored(f"assistant: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "function":
            print(colored(f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))    


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_temperature",
            "description": "Gets the current temperature from a forecast sentence. Returns float: The forecast temperature. Raises ValueError: if the input temperature is invalid/unknown.",
            "parameters": {
                "type": "object",
                "properties": {
                    "temperature": {
                        "type": "number",
                        "description": "The numerical value representing the thermal condition measured in degrees Celsius or Fahrenheit.",
                    },
                },
                "required": ["temperature"],
            },
        }
    },
]            

messages = []
messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."})
messages.append({"role": "user", "content": user_input})

start_time = time.time()
chat_response = chat_completion_request(
    messages, tools=tools
)
assistant_message = chat_response.choices[0].message
messages.append(assistant_message)
end_time = time.time()
elapsed_time = end_time - start_time
print("===========================================================================================================")
print("OPENAI OUTPUT")
print(assistant_message)
print('Time for output: ', elapsed_time)
print("===========================================================================================================")


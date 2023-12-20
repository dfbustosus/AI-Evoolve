"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv
import os
load_dotenv() 
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 0.05,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "hi how are you"
  },
  {
    "role": "model",
    "parts": "Hello! I am here to assist you with your medical appointment"
  },
  {
    "role": "user",
    "parts": "Sure i want to schedule an appointment please"
  },
  {
    "role": "model",
    "parts": "Great! I'm here to assist you with scheduling your medical appointment. Could you please provide me with your phone number so I can look up your customer details?"
  },
  {
    "role": "user",
    "parts": "Yes is 304 111 1145"
  },
  {
    "role": "model",
    "parts": "Could you please provide your full name to proceed with scheduling your appointment?"
  },
  {
    "role": "user",
    "parts": "Yes my name is David Usta"
  },
  {
    "role": "model",
    "parts": "Could you please provide which type of service do you need?"
  },
  {
    "role": "user",
    "parts": "I need a general review with a Doctor"
  },
  {
    "role": "model",
    "parts": "Understood, you've selected general review. What date and time would you prefer for your appointment?"
  },
  {
    "role": "user",
    "parts": "Dec 28 at 4pm please"
  },
  {
    "role": "model",
    "parts": "You've requested a general review, scheduled for December 28th at 4 pm. Is all this information correct?"
  },
  {
    "role": "user",
    "parts": "Yes correct"
  },
  {
    "role": "model",
    "parts": "There is anything else that you need help?"
  },
  {
    "role": "user",
    "parts": "no"
  },
  {
    "role": "model",
    "parts": "Alright, your appointment is confirmed. You'll receive an email shortly with all the details. Is there anything else I can assist you with today?"
  },
  {
    "role": "user",
    "parts": "No thanks"
  },
  {
    "role": "model",
    "parts": "Was nice help you today. Regards!"
  },
  {
    "role": "user",
    "parts": "Hello you can help"
  },
  {
    "role": "model",
    "parts": "Hello! I am here to assist you with your medical appointment"
  },
  {
    "role": "user",
    "parts": "Perfect I need to schedule an appointment"
  },
  {
    "role": "model",
    "parts": "For sure. I'm here to assist you with scheduling your medical appointment. Could you please provide me with your phone number so I can look up your customer details?"
  },
  {
    "role": "user",
    "parts": "Well my phone number is 990901657"
  },
  {
    "role": "model",
    "parts": "Could you please provide your full name to proceed with scheduling your appointment?"
  },
  {
    "role": "user",
    "parts": "My name is Sofia Saenz"
  },
  {
    "role": "model",
    "parts": "Could you please provide which type of service do you need?"
  },
  {
    "role": "user",
    "parts": "I need a cytology"
  },
  {
    "role": "model",
    "parts": "sorry at the moment we have only available GENERAL REVIEW and VACCINATIONS. Do you want to schedule for one of those?"
  },
  {
    "role": "user",
    "parts": "Ok so i want a general review"
  },
  {
    "role": "model",
    "parts": "Understood, you've selected general review. What date and time would you prefer for your appointment?"
  },
  {
    "role": "user",
    "parts": "Dec 29 at 10am please"
  },
  {
    "role": "model",
    "parts": "You've requested a general review, scheduled for December 29th at 10 am. Is all this information correct?"
  },
  {
    "role": "user",
    "parts": "yes"
  },
  {
    "role": "model",
    "parts": "There is anything else that you need help?"
  },
  {
    "role": "user",
    "parts": "No thanks"
  },
  {
    "role": "model",
    "parts": "Alright, your appointment is confirmed. You'll receive an email shortly with all the details. Is there anything else I can assist you with today?"
  },
  {
    "role": "user",
    "parts": "No thanks again"
  },
  {
    "role": "model",
    "parts": "Was a pleasure help you today. Have a great day!"
  },
  {
    "role": "user",
    "parts": "Hi how are you"
  },
  {
    "role": "model",
    "parts": "I am well, thank you for asking. How may I assist you today?"
  },
  {
    "role": "user",
    "parts": "I need a medical appointment"
  },
  {
    "role": "model",
    "parts": "Certainly! I'd be happy to schedule an appointment for you. Could you please provide me with your full name and phone number?"
  },
  {
    "role": "user",
    "parts": "My name is David Usta and my phone os 990901884"
  },
  {
    "role": "model",
    "parts": "Thank you, David. What type of medical appointment do you need?"
  },
  {
    "role": "user",
    "parts": "I need a general review"
  },
  {
    "role": "model",
    "parts": "Sure, a general review appointment can be scheduled. What day and time would you prefer?"
  },
  {
    "role": "user",
    "parts": "Dec 30 at 3pm"
  },
  {
    "role": "model",
    "parts": "Alright, let me confirm the details. You'd like a general review appointment on December 30th at 3 pm. Is that correct?"
  },
  {
    "role": "user",
    "parts": "Yes is correct"
  },
  {
    "role": "model",
    "parts": "Great! Your appointment is confirmed. You'll receive an email shortly with all the details. Is there anything else I can assist you with today?"
  },
  {
    "role": "user",
    "parts": "No thanks"
  },
  {
    "role": "model",
    "parts": "You're welcome. Have a great day, David!"
  }
])

convo.send_message("My name is Ailed and my phone is 978675642")
print(convo.last.text)
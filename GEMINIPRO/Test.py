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
  "temperature": 0,
  "top_p": 0.8,
  "top_k": 2,
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
    "parts": "Hi how are you"
  },
  {
    "role": "model",
    "parts": "Hello! How can I assist you with your car dealer service appointment today?"
  },
  {
    "role": "user",
    "parts": "I want  to schedule an appointment"
  },
  {
    "role": "model",
    "parts": "Great! I'm here to assist you with scheduling your car dealer service appointment. Could you please provide me with your phone number so I can look up your customer details?"
  },
  {
    "role": "user",
    "parts": "Sure my phone number is is 990901883"
  },
  {
    "role": "model",
    "parts": "Could you please provide your full name to proceed with scheduling your appointment?"
  },
  {
    "role": "user",
    "parts": "Sure my name is David Bustos Usta"
  },
  {
    "role": "model",
    "parts": "Could you please provide the license plate number of your vehicle?"
  },
  {
    "role": "user",
    "parts": "Yes is CAL-456"
  },
  {
    "role": "model",
    "parts": "Awesome. Could you please provide the brand, model, and year of your vehicle?"
  },
  {
    "role": "user",
    "parts": "Yes Toyota Hilux 2005"
  },
  {
    "role": "model",
    "parts": "Perfect. What type of service does your vehicle need?"
  },
  {
    "role": "user",
    "parts": "Yeah car wash please"
  },
  {
    "role": "model",
    "parts": "Understood, you've selected CAR WASH. What date and time would you prefer for your appointment?"
  },
  {
    "role": "user",
    "parts": "Dec 30 at 10 am please"
  },
  {
    "role": "model",
    "parts": "You've requested a car wash for your Toyota Hilux, 2005, with the license plate CAL-456, scheduled for December 30th at 10 am. Is all this information correct?"
  },
  {
    "role": "user",
    "parts": "Yes"
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
    "parts": "Hello you can help"
  },
  {
    "role": "model",
    "parts": "Hello! I'm here to assist you with scheduling a car dealer service appointment. How can I help you today?"
  },
  {
    "role": "user",
    "parts": "Well i need an appointment please"
  },
  {
    "role": "model",
    "parts": "Off course! I'd be happy to help you schedule a service appointment for your car. Could you please provide me with your phone number so I can look up your customer details?"
  },
  {
    "role": "user",
    "parts": "my phone is 346 7894561"
  },
  {
    "role": "model",
    "parts": "Could you please provide your full name for the appointment?"
  },
  {
    "role": "user",
    "parts": "Well my name is Joseph Aris"
  },
  {
    "role": "model",
    "parts": "Could you please provide the license plate number of your vehicle?"
  },
  {
    "role": "user",
    "parts": "Yes is MTA-124"
  },
  {
    "role": "model",
    "parts": "Great. Can you provide your brand, make and model from your vehicle?"
  },
  {
    "role": "user",
    "parts": "Yes is Mitsubishi Campero 2008"
  },
  {
    "role": "model",
    "parts": "Awesome. Which type of service do you need?"
  },
  {
    "role": "user",
    "parts": "An oil change please"
  },
  {
    "role": "model",
    "parts": "sorry at the moment we have only available TIRE ROTATION and CAR  WASH. Do you want to schedule for one of those?"
  },
  {
    "role": "user",
    "parts": "sure I want a car wash please"
  },
  {
    "role": "model",
    "parts": "Perfect could you provide a desired date for the appointment"
  },
  {
    "role": "user",
    "parts": "Yes Dec 31 at 4pm"
  },
  {
    "role": "model",
    "parts": "You've requested a car wash for your Mitsubishi Campero, 2008, with the license plate MTA-124, scheduled for December 31th at 4 pm. Is all this information correct?"
  },
  {
    "role": "user",
    "parts": "Yes correct"
  },
  {
    "role": "model",
    "parts": "You've requested a car wash for your Mitsubishi Campero, 2008, with the license plate MTA-124, scheduled for December 30th at 10 am. Is all this information correct?"
  },
  {
    "role": "user",
    "parts": "Yes"
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
    "parts": "Hello good morning"
  },
  {
    "role": "model",
    "parts": "Good morning! How can I assist you with your car dealer service appointment today?"
  },
  {
    "role": "user",
    "parts": "I want to schedule an appointment please"
  },
  {
    "role": "model",
    "parts": "Certainly! I'd be happy to help you schedule a service appointment. Could you please provide me with your phone number so I can look up your customer details?"
  },
  {
    "role": "user",
    "parts": "Yes sure My phone is 31115678965"
  },
  {
    "role": "model",
    "parts": "Thank you for providing your phone number. Could you please confirm your full name for the appointment?"
  },
  {
    "role": "user",
    "parts": "Yeah sure my name is David Bustos Usta"
  },
  {
    "role": "model",
    "parts": "Thank you, David. Could you please provide the license plate number of your vehicle?"
  },
  {
    "role": "user",
    "parts": "Yes is CAL-465"
  },
  {
    "role": "model",
    "parts": "Great! What type of service does your vehicle need?"
  },
  {
    "role": "user",
    "parts": "I need a motor change"
  },
  {
    "role": "model",
    "parts": "I see. Unfortunately, we do not offer engine change services at the moment. Is there anything else I can assist you with?"
  },
  {
    "role": "user",
    "parts": "What services do you have"
  },
  {
    "role": "model",
    "parts": "We offer a range of services for your vehicle, including:\n\n- Oil change\n- Tire rotation\n- Brake inspection\n- Battery check\n- Car wash\n- Detailing\n- Air filter replacement\n- Cabin air filter replacement\n- Wiper blade replacement\n- Headlight restoration\n- Multi-point inspection\n\nIs there a particular service you're interested in?"
  },
  {
    "role": "user",
    "parts": "Ok oil change"
  },
  {
    "role": "model",
    "parts": "Certainly! An oil change is an important service to keep your vehicle running smoothly. When would you like to schedule your appointment?"
  },
  {
    "role": "user",
    "parts": "Dec 10 at 4pm please"
  },
  {
    "role": "model",
    "parts": "Perfect! I have you down for an oil change on December 10th at 4 pm. Please confirm the details are correct before I proceed with the booking."
  },
  {
    "role": "user",
    "parts": "Yes correct"
  },
  {
    "role": "model",
    "parts": "Excellent! Your appointment is confirmed. You'll receive an email shortly with all the details. Is there anything else I can assist you with today?"
  },
  {
    "role": "user",
    "parts": "thanks"
  },
  {
    "role": "model",
    "parts": "You're welcome! If you have any questions or need to make changes to your appointment, feel free to reach out. Have a great day, and we look forward to seeing you soon!"
  }
])

convo.send_message("I want an appointment please")
print(convo.last.text)

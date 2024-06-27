"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os 
import google.generativeai as genai

# **REPLACE THIS WITH YOUR ACTUAL API KEY (See important security notes above!)**
api_key = "AIzaSyCA3PC2Oz926bP_6lnavCBHvB83dZtSvMA" 
genai.configure(api_key=api_key)  

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro", 
  generation_config=generation_config,
  # safety_settings = Adjust safety settings 
  # See https://ai.google.dev/gemini-api/docs/safety-settings 
)

chat_session = model.start_chat(
  history=[
  ] 
)

response = chat_session.send_message("Hi") 

print(response.text) 
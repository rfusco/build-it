from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv() # you can specify a location to your .env file as an argument if it's not at your project root
# Load environment variables
API_KEY = os.getenv("API_KEY")

def initGemini():
  genai.configure(api_key = API_KEY)
  model = genai.GenerativeModel("gemini-1.5-flash")
  return model
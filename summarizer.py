from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_summary(prompt):
    client = genai.Client(api_key=API_KEY)
    print("Google Generative AI client initialized.")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents = prompt)
    
    # print(response)
    
    return response.text
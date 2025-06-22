from google import genai
from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEN_AI_API_KEY')
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

def post_summary(summary):
    client = WebClient(SLACK_BOT_TOKEN)

    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID, 
            text=summary 
        )
        print("Summary posted to Slack channel")
    except Exception as e:
        print(f"Error posting summary to Slack: {e}")
        return
    

def get_summary(prompt):
    client = genai.Client(api_key=API_KEY)
    print("Google Generative AI client initialized.")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents = prompt)
    
    # print(response)

    if response.text:
        post_summary(response.text)
        
    return response.text
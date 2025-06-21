from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()
import os

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")


def get_slack_channel_logs():
    client = WebClient(token=SLACK_BOT_TOKEN)
    print("Slack client initialized.")
    
    response = client.conversations_history(channel=CHANNEL_ID, limit=50)
    print("Fetched channel logs.")
    print(f"Number of messages fetched: {len(response['messages'])}")
        
    chat_log = []
    for message in response['messages']:
        chat = f"- {message.get('text', '')} (User: {message.get('user', 'Unknown')})"
        chat_log.append(chat)
    
    return chat_log
    

    



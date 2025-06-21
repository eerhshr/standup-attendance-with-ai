from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()
import os

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

def simulate_users():
    client = WebClient(token=SLACK_BOT_TOKEN)
    print("Slack client initialized.")
    
    simulated_users = [
    {"name": "Alice", "message": "Hi Im Alice", "emoji": ":woman:"},
    {"name": "Bob", "message": "Hello", "emoji": ":man:"},
    {"name": "Charlie", "message": "Welcome to the channel", "emoji": ":man_office_worker:"}
    ]

    try:
        for user in simulated_users:
            client.chat_postMessage(
            channel=CHANNEL_ID,
            text=user["message"],
            username=user["name"],       # Spoofed display name
            icon_emoji=user["emoji"]    
        )
    except SlackApiError as e:
        assert e.response["error adding user messages"]
    
    #Slack API connection test by sending a message from the bot
    # try:
    #     response = client.chat_postMessage(
    #         channel=CHANNEL_ID,
    #         text="Hello from your app! :tada:"
    #     )
    # except SlackApiError as e:
    #     assert e.response["error"]
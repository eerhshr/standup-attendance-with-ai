from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()
import os

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

def simulate_messages():
    client = WebClient(token=SLACK_BOT_TOKEN)
    print("Slack client initialized.")
    
    #first message to the channel
    # simulated_users = [
    # {"name": "Alice", "message": "Hi Im Alice", "emoji": ":woman:"},
    # {"name": "Bob", "message": "Hello", "emoji": ":man:"},
    # {"name": "Charlie", "message": "Welcome to the channel", "emoji": ":man_office_worker:"}
    # ]
    
    # Simulated users sending standup attendance to the channel
    simulated_users = [
    {"user_id": "UALICE01", "name": "Alice", "message": "I need to take a PTO."},
    {"user_id": "UBOB02", "name": "Bob", "message": "Hello, I'll be joining on time."},
    {"user_id": "UCHARLIE03", "name": "Charlie", "message": "Taking a sick day today."},
    {"user_id": "UDIANA04", "name": "Diana", "message": "Joining late from mobile."},
    {"user_id": "UEMMA05", "name": "Emma", "message": "Won’t be able to make it, I have a conflict"},
    ]

    try:
        for user in simulated_users:
            full_text = f"[{user['user_id']}] {user['message']}" #include user_id in the message to differentiate users because they share same bot id
            client.chat_postMessage(
            channel=CHANNEL_ID,
            text=full_text,
        )
        print("Simulated user messages sent successfully.")
    except SlackApiError as e:
        assert e.response["error adding user messages"]
    
    #Slack API connection test - Post message to the channel from the bot
    # try:
    #     response = client.chat_postMessage(
    #         channel=CHANNEL_ID,
    #         text="Hello from your app! :tada:"
    #     )
    # except SlackApiError as e:
    #     assert e.response["error"]
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import re
from dotenv import load_dotenv

load_dotenv()
import os

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
BOT_ID = os.getenv("SLACK_CHANNEL_BOT_ID")
SLACK_REAL_USER_1 = os.getenv("SLACK_USER_1")
SLACK_REAL_USER_2 = os.getenv("SLACK_USER_2")

def map_users(parsed_chat_log):
    print("Mapping users to names...")
    user_map = {
        SLACK_REAL_USER_1: "Sam",
        SLACK_REAL_USER_2: "David",
        "UEMMA05": "Emma",
        "UDIANA04": "Diana",
        "UCHARLIE03": "Charlie",
        "UBOB02": "Bob",
        "UALICE01": "Alice"
    }
    
    mapped_log = []
    
    for message in parsed_chat_log:
        user_id = message["User"]
        text = message["Text"]
        
        if user_id in user_map:
            name = user_map[user_id]
            mapped_log.append({"User": name, "Text": text})
        else:
            mapped_log.append({"User": user_id, "Text": text})
    
    print("User mapping completed.")
    return mapped_log

def parse_chat_log(chat_log):
    print("Parsing chat log...")
    parsed_log = []
    
    for message in chat_log:
        #print(f"Processing chat logs: {message}")
        user_id = message.split(" (User: ")[-1].rstrip(")")
        text = message.split(" (User: ")[0].strip()
        #print(f"User ID: {user_id}, Text: {text}")
        
        if user_id == BOT_ID:
            match = re.match(r"\[(.*?)\]\s*(.*)", text)
            if match:
                simulated_user_id = match.group(1)
                # print(f"Simulated user id: {simulated_user_id}")
                text = match.group(2).strip()
                # print(f"Parsed text: {text}")
                parsed_log.append({"User" : simulated_user_id, "Text": text})
        else:
            parsed_log.append({"User" : user_id, "Text": text})
            
            #print(f"Simulated user ID: {simulated_user_id}")
                  
    print("Chat logs parsed successfully.")
    #print(parsed_log)
    return parsed_log

def get_slack_channel_logs():
    client = WebClient(token=SLACK_BOT_TOKEN)
    print("Slack client initialized.")
    
    try:
        response = client.conversations_history(channel=CHANNEL_ID, limit=100)
        print("Fetched channel logs.")
        print(f"Number of messages fetched: {len(response['messages'])}")
        
        chat_log = []
        for message in response['messages']:
            chat = f"{message.get('text', '')} (User: {message.get('user', 'Unknown')})"
            chat_log.append(chat)
    
    except SlackApiError as e:
        print(f"Error fetching channel logs: {e.response['error']}")
        
    
    if chat_log:
        try:
            parsed_chat_log = parse_chat_log(chat_log)
        except Exception as e:
            print(f"Error parsing chat log: {e}")
    
    if parsed_chat_log:
        try:
            mapped_chat_log = map_users(parsed_chat_log)
        except Exception as e:
            print(f"Error mapping users: {e}")

    return mapped_chat_log
    

    



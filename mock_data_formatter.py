def format_mock_data_message(messages, user_map):
    #print(f"Slack messages: {message}")
    chat = []
    
    for message in messages:
        user_id = message["user"]
        user_name = user_map.get(user_id, "Unknown User")
        text = message["text"]
        
        chat.append(f"{user_name}: {text}")
    
    chat_log = "\n".join(chat)
    
    #print(chat_log)
    
    prompt = f"""
    From the following Slack messages, list who is attending the standup and who is not.
    Messages:   {chat_log}
    Respond in this format:
    Attending: [list of names]
    Not Attending: [list of names + reasons]
    """.strip()
    
    return prompt
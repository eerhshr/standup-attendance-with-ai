def generate_prompt(chat_log):    
    prompt = f"""
    From the following Slack messages, list who is attending the standup and who is not.
    Messages:   {chat_log}
    Respond in this format:
    Attending: [list of names]
    Not Attending: [list of names + reasons]
    """.strip()
    
    return prompt
    
    
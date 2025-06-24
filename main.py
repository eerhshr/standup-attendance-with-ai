from mock_data import mock_slack_messages, user_map
from mock_data_formatter import  format_mock_data_message
from summarizer import get_summary
from prompt_generator import generate_prompt
import slack_log_fetcher
from simulate_bot_messages import simulate_messages

def main():
    #Simulate messages in Slack channel
    #simulate_messages()
    
    #Get latest messages from Slack channel
    chat_log = slack_log_fetcher.get_slack_channel_logs()
    #print("Chat log fetched from Slack channel")
    #print(chat_log)
    
    #Generate prompt for LLM
    prompt = generate_prompt(chat_log)
    print(f'Standup Attendance Summary: {get_summary(prompt)}')
    
    # Test with mock data
    # prompt = format_mock_data_message(mock_slack_messages, user_map)
    # #print(f'Prompt for LLM: {prompt}')
    # print(f'Standup Attendance Summary: {get_summary(prompt)}')

if __name__ == "__main__":
    main()

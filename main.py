from mock_data import mock_slack_messages, user_map
from mock_data_formatter import  format_mock_data_message
from summarizer import get_summary
from get_prompt import generate_prompt
import get_slack_channel_logs

def main():
    chat_log = get_slack_channel_logs.get_slack_channel_logs()
    print("Chat log fetched from Slack channel:")
    print(chat_log)
    prompt = generate_prompt(chat_log)
    print(f'Prompt for LLM: {prompt}')
    
    # Test with mock data
    # prompt = format_mock_data_message(mock_slack_messages, user_map)
    # #print(f'Prompt for LLM: {prompt}')
    # print(f'Standup Attendance Summary: {get_summary(prompt)}')

if __name__ == "__main__":
    main()

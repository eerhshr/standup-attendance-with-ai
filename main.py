from mock_data import mock_slack_messages, user_map
from formatter import format_message
from summarizer import get_summary

def main():
    prompt = format_message(mock_slack_messages, user_map)
    #print(f'Prompt for LLM: {prompt}')
    print(f'Standup Attendance Summary: {get_summary(prompt)}')

if __name__ == "__main__":
    main()

import os
from pathlib import Path
from dotenv import load_dotenv
from meetingMinder import MeetingMinder


def main():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    token = os.environ['SLACK_TOKEN']
    channel = '#public-test'
    api_url = ''
    handler = MeetingMinder(token, channel, api_url)

    handler.listen('next')  # TODO: remove


if __name__ == '__main__':
    main()

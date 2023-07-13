import re
import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()
slack_token = os.getenv('SLACK_TOKEN')

channel_filter_word = re.compile(r'test')


def filtered_channel():
    client = WebClient(token=slack_token)

    # slack 채널 목록 불러오기
    channels = client.conversations_list()
    channel_list = channels['channels']

    filter_channel = [channel for channel in channel_list
                      if re.search(channel_filter_word, channel['name'])]

    filtered_channels = [
        {
            "text": {
                "type": "plain_text",
                "text": channel['name']
            },
            "value": channel['id']
        }
        for channel in filter_channel
    ]

    return filtered_channels

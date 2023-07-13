import re
import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()
slack_token = os.getenv('SLACK_TOKEN')

client = WebClient(token=slack_token)


def channel_filter():

    channel_filter_name = re.compile(r'test')

    # slack 채널 목록 불러오기
    channels = client.conversations_list()
    channel_list = channels['channels']

    filter_channel = [channel for channel in channel_list
                      if re.search(channel_filter_name, channel['name'])]

    initial_options = [
        {
            "text": {
                "type": "plain_text",
                "text": channel['name']
            },
            "value": channel['id']
        }
        for channel in filter_channel
    ]

    client.chat_postMessage(channel='C05G7S4NGUT', message="test")

    return initial_options

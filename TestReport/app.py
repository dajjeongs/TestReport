from flask import Flask, request
import ssl
import json
import requests
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter
from dotenv import load_dotenv
import os

from TestReport.TestRail import testrail_run
from TestReport import slack_modal_blocks, slack_message_block

ssl._create_default_https_context = ssl._create_unverified_context
app = Flask(__name__)

# 토큰 받아오기
load_dotenv()
slack_token = os.getenv('SLACK_TOKEN')
signing_secret = os.getenv('SIGNING_SECRET')

# Slack 클라이언트 인스턴스 생성
client = WebClient(token=slack_token)
# slack_event_adapter = SlackEventAdapter(signing_secret, '/slack', app)
# BOT_ID = client.api_call("auth.test")['user_id']
#
# @slack_event_adapter.on('message')
# def message(payload):
#     # print(payload)
#     event = payload.get('event', {})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#     text = f"<@{user_id}> 멘션을 받았습니다만, Slash Command를 사용해주세요."
#
#     if BOT_ID != user_id:
#         client.chat_postMessage(channel=channel_id, text=text)


@app.route('/slash', methods=['POST'])
def open_modal():
    # Slack API Endpoint URL
    slack_api_url = 'https://slack.com/api/views.open'

    # 모달 blocks
    slack_modal = slack_modal_blocks.modal_block()

    # slack API에 모달 열기 요청
    response = requests.post(
        slack_api_url,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {slack_token}'
        },
        data=json.dumps(slack_modal)
    )

    # Slack Response
    if response.status_code == 200:
        return '데일리 리포트 작성 중 입니다.'
    else:
        return '모달 열기 실패'


@app.route('/modal_message', methods=['POST'])
def modal_message():
    payload = json.loads(request.form['payload'])
    #print(payload)

    view = payload['view']
    blocks = view['blocks']
    modal_input_value = view['state']['values']

    # slash command 호출 및 모달 작성한  유저 찾기
    user = payload.get('user', {})
    share_user_id = user.get('id')
    share_user = f"<@{share_user_id}>"

    # 메세지 보낼 채널
    global channels_id
    channel_block = blocks[0]['block_id']
    channels_id = modal_input_value[channel_block]['channel_id']['selected_channel']
    print(channels_id)

    # 캘린더에서 선택한 날짜
    date_block = blocks[1]['block_id']
    select_date = modal_input_value[date_block]['day_pick']['selected_date']

    # 멘션 보낼 유저
    try:
        mention_block = blocks[2]['block_id']
        mention = modal_input_value[mention_block]['mention_user']['selected_users'][0]
        mention_user = f"<@{mention}>"
    except:
        mention_user = ""

    # TC 진행률 - 테스트레일 결과 불러오기
    try:
        test_block = blocks[3]['block_id']
        testrail_plan = modal_input_value[test_block]['testrail_plan']['value']
        test_rate = testrail_run.run_result(testrail_plan)
        test_progress = f"*테스트케이스 진행률* :\n{test_rate}"
    except:
        test_progress = " "
    test_result = f"{test_progress}"

    # 현재 진행상황
    progress_block = blocks[4]['block_id']
    progress = modal_input_value[progress_block]['progress']['value']
    daily_progress = f"{progress}"

    # 이슈 및 특이사항
    issue_block = blocks[5]['block_id']
    issue = modal_input_value[issue_block]['issue']['value']
    issue_progress = f"{issue}"

    # 첨부할 링크 - 이슈 대시보드 등...
    try:
        dashboard_block = blocks[6]['block_id']
        dashboard_test = modal_input_value[dashboard_block]['dashboard']['value']
        dashboard = f"• <{dashboard_test}|이슈 대시보드를 참고해주세요.>"
    except:
        dashboard = ""


    # 슬랙 메시지로 텍스트 입력값 전송
    send_slack_message(
        mention_user, select_date, test_result, daily_progress, issue_progress, dashboard, share_user
    )

    return ''


def send_slack_message(mention_user, select_date, test_result, daily_progress, issue_progress, dashboard, share_user):
    slack_message = slack_message_block.slack_message_block(
        mention_user, select_date, test_result, daily_progress, issue_progress, dashboard, share_user
    )

    # 슬랙 메시지 전송을 위한 API Endpoint URL
    slack_message_api_url = 'https://slack.com/api/chat.postMessage'

    # 슬랙에 전달할 메세지
    message = {
        'channel': channels_id,
        'blocks': slack_message
    }

    # slack API에 메세지 전송 요청
    reponse = requests.post(
        slack_message_api_url,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {slack_token}'
        },
        data=json.dumps(message)
    )

    if reponse.status_code == 200:
        print("메시지 전송 완료")
    else:
        print("메시지 전송 실패")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
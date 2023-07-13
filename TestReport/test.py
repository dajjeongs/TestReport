# def mention_bot():
#     data = request.json
#     event = data["event"]
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#
#     #이벤트가 멘션일 경우에만
#     if event.get("type") == "app_mention":
#         response_text = f"<@{user_id}>, 멘션을 받았습니다만, Slash Command를 사용해주세요."
#         message = response_text
#         try:
#             # 응답 전송
#             client.chat_postMessage(channel=channel_id, text=message)
#             print("응답이 성공적으로 전송되었습니다.")
#         except SlackApiError as e:
#             print(f"응답 전송에 실패했습니다. 오류: {e.response['error']}")
#
#     return "", 200




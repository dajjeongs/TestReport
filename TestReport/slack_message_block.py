from datetime import date


def slack_message_block(user_id, feature, test_progress, daily_progress, issue_progress, dashboard, share_user):
    message_blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "QA Daily Report",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{user_id} :calendar: {date.today()} `{feature}` 진행상황 공유드립니다.:pray: \n• 공유자: {share_user}"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{test_progress}"
            }
        },
        # {
        #     "type": "image",
        #     "title": {
        #         "type": "plain_text",
        #         "text": "111"
        #     },
        #     "image_url": image,
        #     "alt_text": "marg"
        #
        # },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*데일리 진행 상황* :\n{daily_progress}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*이슈 및 특이사항* :\n{issue_progress}\n{dashboard}"
            }
        }
    ]

    return message_blocks

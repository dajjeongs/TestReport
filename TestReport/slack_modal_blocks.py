from flask import request
from filtered_channel import filtered_channel


def modal_block():
    channels = filtered_channel()

    slack_modal = {
        'trigger_id': request.form['trigger_id'],
        'view': {
            'type': 'modal',
            'callback_id': 'modal_callback',
            'title': {
                'type': 'plain_text',
                'text': 'Daily Report 작성'
            },
            'blocks': [
                {
                    "type": "input",
                    "block_id": "channel_id",
                    "element": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "리포트를 전송할 채널을 선택하세요"
                        },
                        "options": channels,
                        "action_id": "channel_filter"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Report 전송 채널 선택",
                    }
                },
                {
                    "type": "input",
                    "block_id": "feature_name",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "feature_name",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "QA 진행 중인 피쳐명을 작성해주세요"
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "진행 중인 Feature명"
                    }
                },
                {
                    "type": "input",
                    "block_id": "mention_user",
                    "optional": True,
                    "element": {
                        "type": "multi_users_select",
                        "action_id": "mention_user",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "멘션을 걸 팀원을 선택해 주세요.",
                            "emoji": True
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "멘션 팀원 선택",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "testrail_no",
                    "optional": True,
                    "element": {
                        "type": "number_input",
                        "is_decimal_allowed": False,
                        "action_id": "testrail_no",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "진행 중인 Testrail의 Run 번호를 입력해 주세요. 없으면 비워 주세요."
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Testrail Run No."
                    }
                },
                {
                    "type": "input",
                    "block_id": "daily_progress",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "daily_progress",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "현재 진행 상황을 작성해 주세요."
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Daily 진행 상황",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "issue_progress",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "issue_progress",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "현재 이슈 상태와 특이사항을 작성해 주세요."
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "이슈 및 특이사항",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "dashboard",
                    "optional": True,
                    "element": {
                        "type": "url_text_input",
                        "action_id": "dashboard"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "이슈 대시보드",
                        "emoji": True
                    }
                }
            ],
            'submit': {
                'type': 'plain_text',
                'text': '확인'
            }
        }
    }

    return slack_modal

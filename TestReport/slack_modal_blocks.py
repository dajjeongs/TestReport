from flask import request


def modal_block():
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
                    "label": {
                        "type": "plain_text",
                        "text": "Report 전송 채널 선택"
                    },
                    "element": {
                        "type": "channels_select",
                        "action_id": "channel_id",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "리포트를 전송할 채널을 선택하세요"
                        }
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "feature",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "QA 진행 중인 피쳐명을 작성해주세요"
                        }
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Feature",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "optional": True,
                    "element": {
                        "type": "multi_users_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "멘션을 걸 팀원을 선택해 주세요.",
                            "emoji": True
                        },
                        "action_id": "mention_user"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "멘션 팀원 선택",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "optional": True,
                    "element": {
                        "type": "number_input",
                        "is_decimal_allowed": False,
                        "action_id": "testrail_plan",
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
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "progress",
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
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "issue",
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

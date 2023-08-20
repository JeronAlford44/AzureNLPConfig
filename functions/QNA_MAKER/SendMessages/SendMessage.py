import requests
from flask import jsonify
def SEND_MESSAGE(conversation_id, new_token, uid, msg):
    message_headers = {
        'Authorization': 'Bearer ' + new_token,
        'Content-Type': 'application/json',
        }
    body = {
            "type": "message",
            "text": msg,
            "from": {
                "id": uid
            }
        }
    send_message = requests.post(f'https://directline.botframework.com/v3/directline/conversations/{conversation_id}/activities', headers=message_headers, json= body
        )
    if send_message.status_code > 400:
        return jsonify({"msg": '', "error": f"Error {send_message.status_code}: Could not connect to server"})
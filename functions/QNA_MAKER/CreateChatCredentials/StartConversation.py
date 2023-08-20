import requests
from flask import jsonify
def START_CONVERSATION(token):

    token_headers = {
    'Authorization': 'Bearer ' + token,
    } 
    start_conversation = requests.post('https://directline.botframework.com/v3/directline/conversations', headers=token_headers)
    if start_conversation.status_code > 400:
        return jsonify({"conversation_id": '', "token": '', "error": f"Error {start_conversation.status_code}: Could not connect to server"})
    conversation_id = start_conversation.json().get('conversationId')
    return jsonify({"conversation_id": conversation_id, "token": token, "error": "None"})
    
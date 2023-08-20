import requests
from flask import jsonify
def GET_RESPONSE(conversation_id, new_token):
    message_headers = {
        'Authorization': 'Bearer ' + new_token,
        'Content-Type': 'application/json',
     }
    get_response = requests.get(f'https://directline.botframework.com/v3/directline/conversations/{conversation_id}/activities', headers=message_headers)
    if get_response.status_code > 400:
        return jsonify({"msg": '', "error": f"Error {get_response.status_code} : Could not connect to server"})
    return jsonify({"msg": get_response.json().get('activities')[-1].get('text'), "error": "None"})
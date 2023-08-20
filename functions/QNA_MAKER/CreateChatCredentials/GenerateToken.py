import requests
from flask import jsonify
def GENERATE_TOKEN() -> str:

    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    secret_headers = {
    'Authorization': 'Bearer ' + direct_line_secret,
    }
    #GENERATE TOKEN
    response = requests.post('https://directline.botframework.com/v3/directline/tokens/generate', headers=secret_headers)
    if response.status_code > 400:
        return jsonify({"conversation_id": '', "token": '', "error": f"Error {response.status_code}: Could not connect to server"})
    token = response.json().get('token')
    return token
import requests
from flask import jsonify

def REFRESH_TOKEN(token, uid, msg):
    token_headers = {
        'Authorization': 'Bearer ' + token,
        } 
        #REFRESH TOKEN
    refresh_token = requests.post('https://directline.botframework.com/v3/directline/tokens/refresh', headers=token_headers)
    if refresh_token.status_code > 400:
        return jsonify({"msg": '', "error": f"Error {refresh_token.status_code}: Could not connect to server"})
    new_token = refresh_token.json().get('token')
    
    
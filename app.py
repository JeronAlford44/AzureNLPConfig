from flask import Flask,jsonify, request, redirect
import datetime
import os
from process_msg import process_msg
from flask_cors import CORS
import requests
# from botframework.connector import ConnectorClient
# from botframework.connector.auth import AzureActiveDirectoryAuthentication



app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return 'Home Page Route'

@app.route('/SEND_AND_RECEIVE_MESSAGE', methods = ["POST"])
def SEND_AND_RECEIVE_MESSAGE():
    msg = request.json.get('msg')
    uid = request.json.get('uid')
    token = request.json.get('token')
    conversation_id = request.json.get('conversation_id')
    
    
    
    try:
        token_headers = {
        'Authorization': 'Bearer ' + token,
    
        
        } 
      

        #REFRESH TOKEN
        refresh_token = requests.post('https://directline.botframework.com/v3/directline/tokens/refresh', headers=token_headers)
        
        
        new_token = refresh_token.json().get('token')
    
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
        #SEND ACTIVITY
        send_message = requests.post(f'https://directline.botframework.com/v3/directline/conversations/{conversation_id}/activities', headers=message_headers, json= body
        )
        
        #GET RESPONSE
        get_response = requests.get(f'https://directline.botframework.com/v3/directline/conversations/{conversation_id}/activities', headers=message_headers)
        return jsonify({"msg": get_response.json().get('activities')[-1].get('text')})
    except:
        return "CONNECTION ERROR"

@app.route("/NEW_CHAT_CREDENTIALS", methods = ["POST"])
def GET_CREDENTIALS():
    uid = request.json.get('uid')
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
  
    secret_headers = {
    'Authorization': 'Bearer ' + direct_line_secret,
    
    
    }
    #GENERATE TOKEN
    response = requests.post('https://directline.botframework.com/v3/directline/tokens/generate', headers=secret_headers)
    token = response.json().get('token')
    
    #START CONVERSATION
    token_headers = {
    'Authorization': 'Bearer ' + token,
   
    
    } 
    start_conversation = requests.post('https://directline.botframework.com/v3/directline/conversations', headers=token_headers)
    conversation_id = start_conversation.json().get('conversationId')
    return jsonify({"conversation_id": conversation_id, "token": token})







from flask import Flask,jsonify, request, redirect
import datetime
import os
from process_msg import process_msg
from flask_cors import CORS
import requests
import uuid
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
        if refresh_token.status_code > 400:
            return jsonify({"msg": '', "error": f"Error {refresh_token.status_code}: Could not connect to server"})
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
        if send_message.status_code > 400:
            return jsonify({"msg": '', "error": f"Error {send_message.status_code}: Could not connect to server"})
        #GET RESPONSE
        get_response = requests.get(f'https://directline.botframework.com/v3/directline/conversations/{conversation_id}/activities', headers=message_headers)
        if get_response.status_code > 400:
            return jsonify({"msg": '', "error": f"Error {get_response.status_code} : Could not connect to server"})
        return jsonify({"msg": get_response.json().get('activities')[-1].get('text'), "error": "None"})
    except:
        error = "Error: Could not connect to server" 
        return jsonify({"msg": '', "error": error})

@app.route("/NEW_CHAT_CREDENTIALS", methods = ["POST"])
def GET_CREDENTIALS():
    uid = request.json.get('uid')
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    secret_headers = {
    'Authorization': 'Bearer ' + direct_line_secret,
    }
    #GENERATE TOKEN
    response = requests.post('https://directline.botframework.com/v3/directline/tokens/generate', headers=secret_headers)
    if response.status_code > 400:
        return jsonify({"conversation_id": '', "token": '', "error": f"Error {response.status_code}: Could not connect to server"})
    token = response.json().get('token')
    #START CONVERSATION
    token_headers = {
    'Authorization': 'Bearer ' + token,
    } 
    start_conversation = requests.post('https://directline.botframework.com/v3/directline/conversations', headers=token_headers)
    if start_conversation.status_code > 400:
        return jsonify({"conversation_id": '', "token": '', "error": f"Error {start_conversation.status_code}: Could not connect to server"})
    conversation_id = start_conversation.json().get('conversationId')
    return jsonify({"conversation_id": conversation_id, "token": token, "error": "None"})

@app.route("/TEST_UTTERANCE", methods = ["POST"])
def GET_INTENT():
    uid = request.json.get('uid')
    msg = request.json.get("msg")
    key= "9049133675e64b37975d060c12cdb8a5"
    endpoint='https://plw-bot-2.cognitiveservices.azure.com'
    API_VERSION = '2023-04-01'
    intent_headers = {
        "Ocp-Apim-Subscription-Key": key
    }
    body = {
  "kind": "Conversation",
  "analysisInput": {
    "conversationItem": {
      "id": uuid.uuid4(),
      "participantId": uid,
      "text": msg
    }
  },
  "parameters": {
    "projectName": "plw-bot-2",
    "deploymentName": "deployment1.0",
    "stringIndexType": "TextElement_V8"
  }
}


    response = requests.post(f'{endpoint}/language/:analyze-conversations?api-version={API_VERSION}', headers= intent_headers, body= body)
    return jsonify({"res":response})
    pass




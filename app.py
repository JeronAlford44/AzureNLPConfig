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
# @app.route('/load', methods = ["POST"])


#     return jsonify({"msg" : "Thanks for logging in, how can I assist you today?"})

@app.route('/push_msg_data', methods = ["GET","POST"])
def MessageActivityHandler():
    return "ActivityHandler"
    #START CONVERSATION
    #Send ACTIVITY
    #TRY TO GET RESPONSE
    #IF WEBSOCKET CONNECTION FAILS, RECONNECT TO WEBSOCKET
    #GET RESPONSE
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    msg = request.json.get('msg')
    uid = request.json.get('uid')
    name = request.json.get('name')
    conversation_id = request.json.get('conversation_id')
    locale = request.json.get('locale')
    watermark = request.json.get('watermark')
    """after "/StartConversation" is handled"""
    conversation_id = request.json.get('conversation_id')
    streamUrl = request.json.get('streamUrl').replace("watermark=-&","")
    #.replace('https://', 'wss://').replace('watermark=-&','')
    
 
    
    if not (msg and uid and name):
         return Exception('System Error: Request is invalid and cannot be accessed')
    # headers = {
    # 'Authorization': 'Bearer ' + direct_line_secret,
    # 'Content-Type': 'application/json',
    # "Upgrade": "websocket",
    # "Connection": "upgrade",
    # }
    # data = {
    #     'type': 'message',
    #     'from': {
    #         'id': uid
    #     },
    #     'text': msg
    # }
    # def GET_COVERSATION():
    #     direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    
    #     headers = {
    #     'Authorization': 'Bearer ' + direct_line_secret,
    #     'Content-Type': 'application/json',
        
    #     }
    #     response = requests.post('https://directline.botframework.com/v3/directline/conversations', headers=headers)
    #     return response.json()
@app.route('/RECONNECT', methods = ["POST"])
def RECONNECT():   
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    msg = request.json.get('msg')
    uid = request.json.get('uid')
    name = request.json.get('name')
    conversation_id = request.json.get('conversation_id')
    locale = request.json.get('locale')
    watermark = request.json.get('watermark')
    """after "/StartConversation" is handled"""
    conversation_id = request.json.get('conversation_id')
    streamUrl = request.json.get('streamUrl').replace("watermark=-&","")
    headers = {
    'Authorization': 'Bearer ' + direct_line_secret,
    }
    requests.get(f'https://directline.botframework.com/v3/directline/conversations/{conversation_id}?watermark={watermark}', headers= headers)

    pass
@app.route('/POST_MESSAGE', methods = ["POST"])
def POST_MESSAGE():
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    msg = request.json.get('msg')
    uid = request.json.get('uid')
    # name = request.json.get('name')
   
    # locale = request.json.get('locale')
    # watermark = request.json.get('watermark')
    """after "/StartConversation" is handled"""
    conversation_id = request.json.get('conversation_id')
   
    headers = {
    'Authorization': 'Bearer ' + direct_line_secret,
    'Content-Type': 'application/json',
    
    }
    data = {
        "locale": "en-us",    
        "type": "message",
        "from": {
            "id": uid
        },
        "text": msg
        }
    response = requests.post(f'https://directline.botframework.com/v3/directline/conversations/{conversation_id}/activities', headers=headers, json=data)
    return response
    return response.status_code, response.json()
@app.route('/GET_MESSAGE', methods = ["POST"])
def RETURN_MESSAGE():
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    msg = request.json.get('msg')
    uid = request.json.get('uid')
    name = request.json.get('name')
    conversation_id = request.json.get('conversation_id')
    locale = request.json.get('locale')
    watermark = request.json.get('watermark')
    """after "/StartConversation" is handled"""
    conversation_id = request.json.get('conversation_id')
    streamUrl = request.json.get('streamUrl').replace("watermark=-&","")
    return streamUrl
    headers = {
'Authorization': 'Bearer ' + direct_line_secret,
'Content-Type': 'application/json',
"Upgrade": "websocket",
"Connection": "upgrade",
}   
    
    GET_MSG_RESPONSE = requests.get(streamUrl, headers=headers)
    response = GET_MSG_RESPONSE.json()
    status_code = GET_MSG_RESPONSE.status_code
    watermark = response.get('watermark')
    return response, status_code, response.get('watermark')
#CODE 101 = SWITCHING PROTOCOLS
# Set the parameters for the request




@app.route('/START_CONVERSATION', methods = ["GET"])
def StartConversation():
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
    
   
   
    headers = {
    'Authorization': 'Bearer ' + direct_line_secret,
    'Content-Type': 'application/json',
    
    }
    response = requests.post('https://directline.botframework.com/v3/directline/conversations', headers=headers)
    return response.json()
# # Replace YOUR_DIRECT_LINE_SECRET with your bot's Direct Line secret
#     direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'

#     # Set the headers for the request
#     headers = {
#         'Authorization': 'Bearer ' + direct_line_secret,
#         'Content-Type': 'application/json'
#     }

#     # Set the parameters for the request
#     data = {
#         'type': 'message',
#         'from': {
#             'id': uid
#         },
#         'text': msg
#     }

#     # Send the request to the Direct Line API
#     response = requests.post(f'https://directline.botframework.com/v3/directline/conversations/{name}/activities', json=data, headers=headers)

#     # Print the response status code
#     print(response.status_code)
#     return response.json()
   
#     # def PROCESS_MESSAGE(id, name, msg):
#     # #process message here for chatbot
#     #     return process_msg(msg.replace('%20', ' '), name)
#     #     # return f'Your message is:', msg.replace('%20', ' ')
#     # return PROCESS_MESSAGE(uid, name, msg)
@app.route('/SEND_AND_RECEIVE_MESSAGE', methods = ["POST"])
def SEND_AND_RECEIVE_MESSAGE():
    msg = request.json.get('msg')
    uid = request.json.get('uid')
    token = request.json.get('token')
    conversation_id = request.json.get('conversation_id')
    # direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'
  
    # secret_headers = {
    # 'Authorization': 'Bearer ' + direct_line_secret,
    
    
    # }
    #GENERATE TOKEN
    # response = requests.post('https://directline.botframework.com/v3/directline/tokens/generate', headers=secret_headers)
    # token = response.json().get('token')
    
    #START CONVERSATION
    try:
        token_headers = {
        'Authorization': 'Bearer ' + token,
    
        
        } 
        # start_conversation = requests.post('https://directline.botframework.com/v3/directline/conversations', headers=token_headers)
        # conversation_id = start_conversation.json().get('conversationId')

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
        return get_response.json().get('activities')[-1].get('text')
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







from flask import Flask,jsonify, request, redirect
import datetime
import os
from process_msg import process_msg
from flask_cors import CORS
import requests
from botframework.connector import ConnectorClient
from botframework.connector.auth import AzureActiveDirectoryAuthentication



app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return 'Home Page Route'
# @app.route('/load', methods = ["POST"])


#     return jsonify({"msg" : "Thanks for logging in, how can I assist you today?"})

@app.route('/push', methods = ["POST"])
def RECEIVE_MESSAGE():
    msg = request.json.get('msg')
    uid = request.json.get('id')
    name = request.json.get('name')
    if not (msg and id and name):
         return Exception('System Error: Request is invalid and cannot be accessed')
   # Replace YOUR_CLIENT_ID and YOUR_TENANT_ID with your own values
    CLIENT_ID = '10d9a82c-a84d-4891-91f5-e7f3f18cd5f2'
    TENANT_ID = '0376eb4b-c206-4056-9061-e342dc2ecda8'
    return CLIENT_ID
    # Get the access token for the Bot Framework API
    auth = AzureActiveDirectoryAuthentication(CLIENT_ID, TENANT_ID)
    access_token = auth.get_access_token()

    # Create a ConnectorClient
    client = ConnectorClient(auth, base_url='https://directline.botframework.com/v3/directline')

    # Set the parameters for the request
    conversation_id = name
    activity = {
        'type': 'message',
        'from': {
            'id': uid
        },
        'text': msg
    }

    # Send the message
    response = client.conversations.send_to_conversation(conversation_id, activity)

    # Print the response
    return (response)
  

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
   
    
    
       








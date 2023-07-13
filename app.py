from flask import Flask,jsonify, request, redirect
import datetime
import os
from process_msg import process_msg
from flask_cors import CORS
import requests



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
         raise Exception('System Error: Request is invalid and cannot be accessed')
   
  

# Replace YOUR_DIRECT_LINE_SECRET with your bot's Direct Line secret
    direct_line_secret = 'u_6jUVjegJI.qhi8oQuDDrXQ5wUv9fj6Lvy44Z7qLjZzUA1yxiSOIDE'

    # Set the headers for the request
    headers = {
        'Authorization': 'Bearer ' + direct_line_secret,
        'Content-Type': 'application/json'
    }

    # Set the parameters for the request
    data = {
        'type': 'message',
        'from': {
            'id': uid
        },
        'text': msg
    }

    # Send the request to the Direct Line API
    response = requests.post('https://directline.botframework.com/v3/directline/conversations/{name}/activities', json=data, headers=headers)

    # Print the response status code
    print(response.status_code)
    return response.json()
    # def PROCESS_MESSAGE(id, name, msg):
    # #process message here for chatbot
    #     return process_msg(msg.replace('%20', ' '), name)
    #     # return f'Your message is:', msg.replace('%20', ' ')
    # return PROCESS_MESSAGE(uid, name, msg)
   
    
    
       




# @app.route('/process-msg/id=<string:id>/name=<string:name>/msg=<string:msg>')
# def PROCESS_MESSAGE(id, name, msg):
#     #process message here for chatbot
#     process_msg(msg.replace('%20', ' '), name)
#     return f'Your message is:', msg.replace('%20', ' ')


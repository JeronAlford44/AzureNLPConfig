from flask import Flask,jsonify, request, redirect
import datetime
import os
from process_msg import process_msg
from flask_cors import CORS

# import firebase_admin
# from firebase_admin import credentials, firestore, initialize_app



app = Flask(__name__)
CORS(app)
# cred = credentials.Certificate(os.environ.get('FIREBASE_CREDENTIALS'))
# if cred is not None: 
#     default_app = initialize_app(cred)
# else:
#     quit()
# db = firestore.client()

@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/push', methods = ["POST"])
def RECEIVE_MESSAGE():
    msg = request.json.get('msg')
    id = request.json.get('id')
    name = request.json.get('name')
    if not (msg or id or name):
         raise Exception('System Error: Request is invalid and cannot be accessed')
    def PROCESS_MESSAGE(id, name, msg):
    #process message here for chatbot
        return process_msg(msg.replace('%20', ' '), name)
        return f'Your message is:', msg.replace('%20', ' ')
    return PROCESS_MESSAGE(id, name, msg)
   
    
    
       




# @app.route('/process-msg/id=<string:id>/name=<string:name>/msg=<string:msg>')
# def PROCESS_MESSAGE(id, name, msg):
#     #process message here for chatbot
#     process_msg(msg.replace('%20', ' '), name)
#     return f'Your message is:', msg.replace('%20', ' ')


from flask import Flask,jsonify, request, redirect
import datetime
import os

from flask_cors import CORS
import requests
import uuid
from functions.NLP.PredictionRequest import CREATE_PREDICTION_REQUEST
# from botframework.connector import ConnectorClient
# from botframework.connector.auth import AzureActiveDirectoryAuthentication
from functions.QNA_MAKER.CreateChatCredentials.GenerateToken import GENERATE_TOKEN
from functions.QNA_MAKER.CreateChatCredentials.StartConversation import START_CONVERSATION

from functions.QNA_MAKER.ReceiveMessages.GetResponse import GET_RESPONSE
from functions.QNA_MAKER.SendMessages.RefreshToken import REFRESH_TOKEN
from functions.QNA_MAKER.SendMessages.SendMessage import SEND_MESSAGE



app = Flask(__name__)
CORS(app)


@app.route('/', methods = ["GET"])
def home():
    return 'Home Page Route'

@app.route('/HANDLE_ACTIVITY', methods = ["POST"])
def HANDLE_ACTIVITY():
    
    msg = request.json.get('msg')
    uid = request.json.get('uid')
    token = request.json.get('token')
    conversation_id = request.json.get('conversation_id')
    
    
    
    try:
        #REFRESH TOLEN
        new_token = REFRESH_TOKEN(token, uid, msg)
        #SEND MESSAGE
        SEND_MESSAGE(conversation_id, new_token, uid, msg)
        #GET RESPONSE
        response = GET_RESPONSE(conversation_id, new_token)
        return response
    except:
        error = "Error: Could not connect to server" 
        return jsonify({"msg": '', "error": error})

@app.route("/NEW_CHAT_CREDENTIALS", methods = ["POST"])
def GET_CREDENTIALS():
    #GENERATE A TOKEN
    token = GENERATE_TOKEN()
    #START CONVERSATION WITH AZURE
    return START_CONVERSATION(token)
    
   

@app.route("/TEST_UTTERANCE", methods = ["POST"])
def GET_INTENT():
    uid = str(request.json.get('uid'))
    msg = str(request.json.get("msg"))
    sessionId = str(request.json.get("sessionId"))
    return CREATE_PREDICTION_REQUEST(uid, msg, sessionId)
    pass




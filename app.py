from flask import Flask,jsonify, request, redirect
import datetime
import os

# import firebase_admin
# from firebase_admin import credentials, firestore, initialize_app



app = Flask(__name__)
# cred = credentials.Certificate(os.environ.get('FIREBASE_CREDENTIALS'))
# if cred is not None: 
#     default_app = initialize_app(cred)
# else:
#     quit()
# db = firestore.client()

@app.route('/')
def home():
    return 'Home Page Route'

@app.route("/users/id=<string:id>/msg=<string:msg>", methods=['POST', 'GET'])
def ADD_USER_MSG_BY_ID(id, msg):
    # db_ref = db.collection('Users').document(id)
    # db_ref.update({
    #     f'info.ChatLogs.{msg}': firestore.SERVER_TIMESTAMP
    # }
    # )
    return jsonify({
        f"{msg}": datetime.datetime.now().timestamp()
    }
    )
@app.route('/push', methods = ["POST"])
def RECEIVE_MESSAGE():
    msg = request.json.get('msg')
    if msg is not None:
        return redirect(f'/process-msg/msg={msg}')
    else:
        raise Exception('System Error: Request is invalid and cannot be accessed')

@app.route('/get', methods = ["GET"] )
def getjson():
    return jsonify({"msg": 'Thanks for using our api'})


@app.route('/process-msg/msg=<string:msg>')
def PROCESS_MESSAGE(msg):
    #process message here for chatbot
    return f'Your message is:', msg.replace('%20', ' ')


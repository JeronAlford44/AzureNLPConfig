from flask import Flask,jsonify, request
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
def processjson():
    return request.json['msg']

@app.route('/get')
def getjson():
    return jsonify({"msg": 'Thanks for using our api'})

@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


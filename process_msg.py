from flask import jsonify
def process_msg(message):
    if message == "Hello World":
        return jsonify({"msg" : "Good day to you"})
    return jsonify({"msg" : "Sorry, I did not understand your message. Please enter a new message"})
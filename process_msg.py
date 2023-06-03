from flask import jsonify
def process_msg(message, name):
    if message == "Hello World":
        return jsonify({"msg" : f"Good day to you {name}"})
    return jsonify({"msg" : "Sorry, I did not understand your message. Please enter a new message"})
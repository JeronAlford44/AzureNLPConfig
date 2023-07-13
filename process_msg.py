from flask import jsonify
def process_msg(message, name):
    if message == "Hello World":
        return jsonify({"msg" : f"Good day to you {name}"})
    if message == "How are you?":
        return jsonify({"msg": "I am doing great, how about you?"})
    if message == "What is my name?": 
        return jsonify({"msg": f"The name you registered with is {name}"})
    return jsonify({"msg" : "Thanks for logging in, how can I assist you today?"})


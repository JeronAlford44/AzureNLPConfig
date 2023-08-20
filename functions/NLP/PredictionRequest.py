import requests
def CREATE_PREDICTION_REQUEST(uid, msg, sessionId):
    key= "9049133675e64b37975d060c12cdb8a5"
    endpoint='https://plw-bot-2.cognitiveservices.azure.com'
    API_VERSION = '2023-04-01'
    intent_headers = {
        "Ocp-Apim-Subscription-Key": key,
          'Content-Type': 'application/json',
    }
    data = {
  "kind": "Conversation",
  "analysisInput": {
    "conversationItem": {
      "id": sessionId,
      "participantId": uid,
      "text": msg
    }
  },
  "parameters": {
    "projectName": "plw-bot-2-botv1",
    "deploymentName": "deployment1.0",
    "stringIndexType": "TextElement_V8"
  }
}
    response = requests.post(f'{endpoint}/language/:analyze-conversations?api-version={API_VERSION}', headers= intent_headers,json = data)
    return response.json()

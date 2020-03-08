import random
import os
from wildlife_facts import random_mwl_fact
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET'])
def handle_verification():
    if(request.args.get('hub.verify_token') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get("hub.challenge")
    else:
        print("Wrong token")
        return "Error, wrong validation token"
    

@app.route("/", methods=['POST'])
def receive_message():
    # get whatever message a user sent the bot
   output = request.get_json()
   for event in output['entry']:
      print(event)
      messaging = event['messaging']
      for message in messaging:
        if message.get('message'):
            #Facebook Messenger ID for user so we know where to send response back to
            recipient_id = message['sender']['id']
            if (message['message'].get('text')) == "fact":
                send_message(recipient_id, random_mwl_fact)
            if message['message'].get('text'):
                response_sent_text = get_message()
                send_message(recipient_id, response_sent_text)
            #if user sends us a GIF, photo,video, or any other non-text item
            if message['message'].get('attachments'):
                response_sent_nontext = get_message()
                send_message(recipient_id, response_sent_nontext)
        return "Message Processed"
            


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()


## TO RUN:
## in console
## python app.py
## in ngrok
## ngrok http 5000 (or port no)


## Deploys to Heroku Not Made Automatically; do manually
## https://marine-wildlife-fans.herokuapp.com/
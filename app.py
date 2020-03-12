import random
import os
from flask import Flask, request
from pymessenger.bot import Bot
from wildlife_facts import random_mwl_fact

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"

@app.route("/", methods=['POST'])
def receive_message():
    output = request.get_json()
    for event in output['entry']:
       messaging = event['messaging']
       for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id']  # Recipient ID to know who to message
                if message['message'].get('text'):      # If message is a text
                    text = message['message'].get('text')
                    if text == "facts":
                        facts = random_mwl_fact()
                        send_message(recipient_id, facts)
                        return "Message Processed"
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


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
from marine_wildlife_fans import app, send_message, get_random_message, VERIFY_TOKEN
from marine_wildlife_fans.wildlife_facts import random_mwl_fact
from flask import request

# VERIFY BOT
@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"

# HANDLE MESSAGES
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
                    response_sent_text = get_random_message()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_random_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

    # if recipient id in postgres
        # set state to state from user
        # handle message (userstate, income message)
            # answer
        # change user state

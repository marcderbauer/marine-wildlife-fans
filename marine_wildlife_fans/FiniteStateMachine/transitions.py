from app import send_message
from FiniteStateMachine.statemachine import StateMachine, StateMachineUser
from wildlife_facts import random_mwl_fact
from pymessenger.bot import Bot
# import app
# TODO: replace comparisons with regex

id_test = [12345 ,69420, 210320]
users = {} # Dict of StateMachineUsers

def start_transitions(txt, user_id):
    txt = txt.upper() ### Move over to statemachine? # General processing function(to upper, strip whitespace,...)
    if txt == "ANIMAL FACT":
        send_message(random_mwl_fact(), user_id)
        newState = "animal_fact_state"
    elif txt == "PICTURE":
        # send message random picture
        newState = "start_state"
    elif txt == "WILDLIFE":
        print("Donate to one of these following Charities: xxx") #change to send message
        newState = "start_state"
    elif txt ==  "CONTACT":
        print("Would you want to talk to a human or would want us to send an email?")
        newState = "contact_state"
    elif txt == None:
        return
    else:
        #### REPLACE WITH SEND MESSAGE ####
        print("Sorry I didn't understand that")
        newState = "start_state"
    return(newState)

def animal_fact_transitions(txt, user_id):
    txt = txt.upper()
    if txt == "ANOTHER ONE":
        # send animal fact
        newState = "animal_fact_state"
    elif txt == "BACK":
        # back to first state
        newState = "start_state"
    else:
        #### REPLACE WITH SEND MESSAGE ####
        print("Sorry I didn't understand that")
        newState = "start_state"
    return(newState)

def contact_transitions(txt, user_id):
    txt = txt.upper()
    if txt == "HUMAN":
        print("We'll get back to you soon, just look out for your messages!")
        newState = "start_state"
    elif txt == "EMAIL": # process txt to make e-mail the same
        print("What email adress should we send the email to?")
        newState = "contact_state_2"
    else:
        #### REPLACE WITH SEND MESSAGE ####
        print("Sorry I didn't understand you! Ting bu dong")
        newState = "contact_state"
    return(newState)

def contact_transitions_2(txt, user_id):
    email = process_email(txt)
    print("We'll send you an email shortly, thanks a lot fellow Marine Wildlife friend!")
    print("Anything else we can help you with?")
    newState = "start_state"
    return newState

def process_email(txt):
    # do something
    return txt

if __name__ == "__main__":
    for id in id_test:
        users[id] = StateMachineUser(id)
    

"""
    users[id_test[0]].state = m.run("animal fact", user=users[id_test[0]])
    print(users[id_test[0]].state)
    m.run("contact", user=users[id_test[0]])
"""
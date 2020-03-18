import random
import os
import psycopg2
from flask import Flask, request
from pymessenger.bot import Bot
from marine_wildlife_fans.FiniteStateMachine import statemachine, transitions

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
DATABASE_URL = os.environ['DATABASE_URL']
bot = Bot(ACCESS_TOKEN)

app = Flask(__name__)

# TODO
# change to be able to work on multiple apps


###TODO: 
# if haven't recieved a message from that user yet, create new StateMachineUser Instance with userid (and empty state ?)
# if have recieved before, access user and continue with that current state
#  -> create new method for it, don't want to overcomplicate shit
# THEN: Process message!

#chooses a random message to send to the user
def get_random_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


#### PACKAGE ALL DEFINED TRANSITIONS INTO A FUNCTION AND CALL IT HERE?
# maybe a dict of transitions
# use self.handlers? from statemachine?
# input: user(id or whole object) -> see below

def get_user(user_id):
    user = "CHANGE THIS TO GET THE USER FROM POSTGRES"
    # get row of specified user id
    # convert back to object ?
    # or better to just get information, and change directly in POSTGRES
    # => Probably better
    return user

import marine_wildlife_fans.views # Verify connection to FB and handle incoming messages


# Finite State Machine
m = statemachine.StateMachine()
m.add_state("start_state", transitions.start_transitions)
m.add_state("animal_fact_state", transitions.animal_fact_transitions)
m.add_state("contact_state", transitions.contact_transitions)
m.add_state("contact_state_2", transitions.contact_transitions_2)
m.set_start("start_state")
# Postgres
try:    
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")

if __name__ == "__main__":
    app.run()
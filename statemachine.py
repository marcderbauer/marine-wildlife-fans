# Modified Statemachine, original taken from https://www.python-course.eu/finite_state_machine.php

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None

    def add_state (self, name, handler, end_state=0):
        name =  name.upper()
        self.handlers[name] = handler
    
    def set_start (self, name):
        self.startState = name.upper()

    def run(self, message, user):
        # be sure to set start before running!
        
        if not user.state:
            handler = self.handlers[self.startState]
        else:
            handler = self.handlers[user.state.upper()]

        user.state = handler(message, user.user_id)
        handler = self.handlers[user.state.upper()]
        return user.state


class StateMachineUser:
    def __init__(self, user_id, state = None):
        self.user_id = user_id
        self.state = state

# Generalized Statemachine, taken from https://www.python-course.eu/finite_state_machine.php

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state (self, name, handler, end_state=0):
        name =  name.upper() # ALLCAPS NAME
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)
    
    def set_start (self, name):
        self.startState = name.upper() # Set start State (ALLCAPS)

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError ("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError ("at least one state muse be an end_state")

        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                print("reached", newState)
                break
            else:
                handler = self.handlers[newState.upper()]
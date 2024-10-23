
# Finite Automation
# Mod 3 #standard

##==========================================================================
# states
class State:
    def __init__(self, FSM):
        self.FSM = FSM

    def Enter(self):
        print("Entering")
        
    def Execute(self):
        print("Executing")

    def Exit(self):
        print("Exiting")

class S0(State):
    def __init__(self, FSM):
        super(S0, self).__init__(FSM)

    def Enter(self):
        print("Entering State S0 (remainder 0 mod 3)")

    def Execute(self):
        if self.FSM.input_symbol == '0':
            print("Read '0' in S0, staying in S0")
            self.FSM.to_transition = "S0"
        elif self.FSM.input_symbol == '1':
            print("Read '1' in S0, transitioning to S1")
            self.FSM.to_transition = "S1"

# State S1: Sum of 1's gives remainder 1 when divided by 3
class S1(State):
    def __init__(self, FSM):
        super(S1, self).__init__(FSM)

    def Enter(self):
        print("Entering State S1 (remainder 1 mod 3)")

    def Execute(self):
        if self.FSM.input_symbol == '0':
            print("Read '0' in S1, staying in S1")
            self.FSM.to_transition = "S1"
        elif self.FSM.input_symbol == '1':
            print("Read '1' in S1, transitioning to S2")
            self.FSM.to_transition = "S2"

# State S2: Sum of 1's gives remainder 2 when divided by 3
class S2(State):
    def __init__(self, FSM):
        super(S2, self).__init__(FSM)

    def Enter(self):
        print("Entering State S2 (remainder 2 mod 3)")

    def Execute(self):
        if self.FSM.input_symbol == '0':
            print("Read '0' in S2, staying in S2")
            self.FSM.to_transition = "S2"
        elif self.FSM.input_symbol == '1':
            print("Read '1' in S2, transitioning to S0")
            self.FSM.to_transition = "S0"

##=============================================================================
# transitions

class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print("Transitioning to", self.toState)
##=============================================================================
# Finite State Machine (FSM)

class FSM(object):
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None
        self.to_transition = None
        self.input_symbol = None

    def AddState(self, stateName, state):
        self.states[stateName] = state

    def SetState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def Execute(self):
        if self.to_transition:
            self.curState.Exit()
            self.SetState(self.to_transition)
            self.curState.Enter()
            self.to_transition = None
        self.curState.Execute()

##====================================================================================
# A machine to handle binary input

class BinaryFA(FSM):
    def __init__(self):
        self.states = {
            "S0": 0,  
            "S1": 1,
            "S2": 2 
        }
        self.transitions = {
            ("S0", '0'): "S0", ("S0", '1'): "S1",
            ("S1", '0'): "S2", ("S1", '1'): "S0",
            ("S2", '0'): "S1", ("S2", '1'): "S2"
        }
        self.curState = "S0"

    def ProcessInput(self, input_string):
        for symbol in input_string:
            self.curState = self.transitions[(self.curState, symbol)]

    def Output(self):
        # Print the output value based on the current state
        print(f"Output value for state {self.curState}: {self.states[self.curState]}")


if __name__ == "__main__":
    fsm = BinaryFA()
    input_string = "1010"
    fsm.ProcessInput(input_string)
    fsm.Output() 

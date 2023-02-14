class Finite_Automaton:
    # Constructor of Finite_Automaton class
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F
    # Method which check if word is valid
    def string_belongs_to_language(self,input_string):
        # Set the current state to the initial state
        current_state = self.q0

        # For each symbol in the input string, find the next state using the delta function
        for symbol in input_string:
            if (current_state, symbol) in self.delta:
                current_state = self.delta[(current_state, symbol)]
            else:
                continue

        # If the current state is in the set of final states, return True
        if current_state in self.F:
            return True
        else:
            return False

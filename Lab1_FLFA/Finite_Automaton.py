class Finite_Automaton:
    # Constructor of Finite_Automaton class
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F
    # Method which check if word is valid
    def string_belongs_to_language(self, input_string):
        # Set the current state to the initial state
        current_state = self.q0
        nr = 0
        # For each symbol in the input string, find the next state using the delta function
        for symbol in input_string:
            if ((current_state[0], symbol) in self.delta) and (nr != len(input_string)-1):
                current_state = self.delta[(current_state[0], symbol)]
            elif nr == len(input_string) - 1:
                if len(current_state) > 1:
                    # If the current state is in the set of final states, return True
                    if current_state[len(current_state)-1] in self.F:
                        return True
                    else:
                        return False
                else:
                    if current_state[0] in self.F:
                        return True
                    else:
                        return False
            nr += 1

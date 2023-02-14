import Finite_Automaton


class Grammar:
    # Constructor of Grammar class
    def __init__(self, V_N, V_T, P):
        self.V_N = V_N
        self.V_T = V_T
        self.P = P

    # Method which generate words corresponding to rules
    def generate_string(self):
        import random
        # Start of the word
        word = "S"
        # Set of final states
        final_states = ["b", "a"]
        # While loop which create a random word
        while word[-1] not in final_states:
            options = []
            for vn, prod in self.P.items():
                if vn == word[-1]:
                    options += prod
            if not options:
                return None
            production = random.choice(options)
            word = word[:-1] + production
        return word

    # Method which transfer from grammar class to finite automaton class
    def to_finite_automaton(self):
        # Initiate finite set of states
        Q = set(self.V_N)
        # Initiate the alphabet
        Sigma = set(self.V_T)
        # Initiate the initial state
        q0 = "S"
        # Initiate the set of final states
        F = ["b", "a"]
        # Initiate the transition function
        delta = {}
        for vn, prod in self.P.items():
            for symbol in prod:
                if symbol[1:] != "":
                    delta[(vn, symbol[0])] = symbol[1:]
                else:
                    delta[(vn, symbol[0])] = symbol[0]

        # Call the constructor of Finite Automaton class
        return Finite_Automaton.Finite_Automaton(Q, Sigma, delta, q0, F)

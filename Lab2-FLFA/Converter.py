class Converter:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def is_dfa(self):
        if not self.Q or not self.Sigma:
            return False
        for state in self.Q:
            for symbol in self.Sigma:
                if (state, symbol) not in self.delta or self.delta[(state, symbol)] not in self.Q:
                    return False
        if self.q0 not in self.Q:
            return False
        if not set(self.F).issubset(set(self.Q)):
            return False
        return True

    def to_dfa(self):
        if self.is_dfa():
            return self

        dfa_states = set()
        dfa_accept_states = set()
        dfa_transitions = dict()
        state_queue = [frozenset([self.q0])]
        while state_queue:
            current_states = state_queue.pop(0)
            dfa_states.add(current_states)
            if any(state in self.F for state in current_states):
                dfa_accept_states.add(current_states)
            for symbol in self.Sigma:
                next_states = set()
                for state in current_states:
                    next_states |= set(self.delta.get((state, symbol), set()))
                if next_states:
                    next_states = frozenset(next_states)
                    dfa_transitions[(current_states, symbol)] = next_states
                    if next_states not in dfa_states:
                        state_queue.append(next_states)

        dfa = Converter(dfa_states, self.Sigma, dfa_transitions, self.q0, dfa_accept_states)
        return dfa

    def to_grammar(self):
        productions = dict()
        for state in self.Q:
            for symbol in self.Sigma:
                next_states = self.delta.get((state, symbol), set())
                for next_state in next_states:
                    if next_state in self.F:
                        if state not in productions:
                            productions[state] = set()
                        productions[state].add(symbol)
                    else:
                        if next_state not in productions:
                            productions[next_state] = set()
                        productions[next_state].add(symbol + ' ' + state)
        start_symbol = self.q0
        if start_symbol in productions:
            productions['S'] = productions[start_symbol]
            del productions[start_symbol]
            for state in self.Q:
                for symbol in self.Sigma:
                    next_states = self.delta.get((state, symbol), set())
                    for next_state in next_states:
                        if state in productions and symbol + state in productions[state]:
                            if next_state not in productions:
                                productions[next_state] = set()
                            productions[next_state].add(symbol + ' S')
        else:
            start_symbol = 'S'
            productions[start_symbol] = set()
            for accept_state in self.F:
                productions[start_symbol].add('eps' + accept_state)

        return start_symbol, productions
# Topic: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata
### Author: Rotaru Ion 

## Objectives:
1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.
## Implementation
* Converter class
    ```python
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
    ```
## Conclusion
In this laboratory work I learned and implemented regular grammar and a finite automaton. 
I strengthened my knowledge in this field and received new experience in coding. In some moments, errors appeared that were a big obstacle and because of which
I had to review all the code and study new things.
## References
* Regular Expressions, Regular Grammar and Regular Languages: https://www.geeksforgeeks.org/regular-expressions-regular-grammar-and-regular-languages/?ref=lbp
* Deterministic finite automaton: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
* Nondeterministic finite automaton: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
                 

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
In the method "is_dfa" it is checked whether the finite automaton is deterministic or non-deterministic. Each set is checked if it corresponds to the rules     that are in a deterministic finite automaton.
```python
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
```
In the "to_dfa" method, the control method is called to see if the automaton is non-deterministic. If not, the necessary steps are taken to transform an NDFA into a DFA. In order to form a DFA from the NDFA, a loop is formed that checks step by step whether the deltas correspond to a DFA. If the delta does not match, then a new set is formed that includes all the necessary states and is grouped together with the terminal symbol in the dictionary
```python
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

```
In the "to_grammar" method, the process of converting an FA into a Grammar is carried out by simply transferring from the sets of an FA to the sets required for     a Grammar. In this method, the simple transfer of the sets Q, Sigma, delta, q0, F is done in the sets that correspond to a grammar: Vn, Vt, P, S.
```python
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
In this method, the grammar is classified by passing through a series of conditions that call for control methods starting from the strictest and ending with the most unrestricted
```python
    def classify_grammar(self, P):

        if self.is_regular(P):
            return "Type 3"
        if self.is_context_free(P):
            return "Type 2"
        if self.is_context_sensitive(P):
            return "Type 1"
        if self.is_unrestricted(P):
            return "Type 0"

        return "Not in Chomsky hierarchy"
```
These methods control the type of grammar by performing the necessary steps and if it does not match they return "false", but the "is_unrestricted" method only returns "true" because it corresponds to type 0 which receives any type of grammar. The "is_regular" method is for type 3, "is_context_sensitive" for type 2 and "is_context_free" for type 1.
```python
    def is_unrestricted(self, P):

        return True

    def is_context_sensitive(self, P):

        for lhs, rhs_list in P.items():
            for rhs in rhs_list:
                if len(rhs) < len(lhs):
                    return False
                for i, symbol in enumerate(rhs):
                    if symbol in P and i != len(rhs) - 1:
                        if len(rhs) <= len(lhs):
                            return False
        return True

    def is_context_free(self, P):

        for lhs, rhs_list in P.items():
            if len(lhs) != 1 or not lhs.isupper():
                return False
            for rhs in rhs_list:
                for symbol in rhs:
                    if symbol not in P and not symbol.islower():
                        return False
        return True

    def is_regular(self, P):

        for lhs, rhs_list in P.items():
            if not lhs.isupper():
                return False
            for rhs in rhs_list:
                if len(rhs) == 1 and rhs.islower():
                    continue
                elif len(rhs) == 2 and rhs[0].islower() and rhs[1].isupper():
                    continue
                else:
                    return False
        return True
```
## Conclusion
In this laboratory work I learned and implemented converter from NFA to DFA or from FA to Regular Grammar. 
I learned how to determine if an FA is deterministic or non-deterministic. I found out the steps to convert an NDFA to a DFA
## References
* Regular Expressions, Regular Grammar and Regular Languages: https://www.geeksforgeeks.org/regular-expressions-regular-grammar-and-regular-languages/?ref=lbp
* Deterministic finite automaton: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
* Nondeterministic finite automaton: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
                 

import Converter

Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b', 'c'}
q0 = 'q0'
delta = {
            ('q0', 'a'): {'q0', 'q1'},
            ('q1', 'b'): {'q2'},
            ('q2', 'c'): {'q3'},
            ('q3', 'c'): {'q3'},
            ('q2', 'a'): {'q2'}
        }
F = {'q3'}
conv = Converter.Converter(Q, Sigma, delta, q0, F)
print(conv.is_dfa())
dfa = conv.to_dfa()
print(f"Set of states: {dfa.Q}")
print(f"Set of transition function: {dfa.delta}")
print(f"Set of initial state: {dfa.q0}")
print(f"Set of  final states: {dfa.F}")
grammar = conv.to_grammar()
print(f"Set of regular grammar productions: {grammar}")
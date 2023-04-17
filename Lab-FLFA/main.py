import Grammar

V_N = {'S', 'A', 'B', 'C', 'D'}
V_T = {'a', 'b', 'd'}
P = {
    'S': {'dB', 'AC'},
    'A': {'d', 'dS', 'aBdB'},
    'B': {'a', 'aA', 'AC'},
    'C': {'bC', 'ε'},
    'D': {'ab'}
}
grammar = Grammar.Grammar(V_N, V_T, P)
grammar.cnf()
print(V_N)
print(V_T)
print(P)

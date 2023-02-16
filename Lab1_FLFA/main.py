import Grammar

V_N = {'S', 'B', 'C', 'D', 'X'}
V_T = {'a', 'b', 'c'}
P = {
    "S": ["aB"],
    "B": ["bS", "aC", "bX"],
    "C": ["bD"],
    "D": ["aX", "bC", "cS"],
    "X": " "
}

grammar = Grammar.Grammar(V_N, V_T, P)

finite_automaton = grammar.to_finite_automaton()

s1 = grammar.generate_string()
s2 = grammar.generate_string()
s3 = grammar.generate_string()
s4 = grammar.generate_string()
s5 = grammar.generate_string()
print(s1)

print("s1 is " + str(finite_automaton.string_belongs_to_language(s1)))
print("s2 is " + str(finite_automaton.string_belongs_to_language(s2)))
print("s3 is " + str(finite_automaton.string_belongs_to_language(s3)))
print("s4 is " + str(finite_automaton.string_belongs_to_language(s4)))
print("s5 is " + str(finite_automaton.string_belongs_to_language(s5)))

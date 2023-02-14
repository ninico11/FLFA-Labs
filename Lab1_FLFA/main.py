import Grammar
# Set of non-terminal symbols
V_N = {'S', 'B', 'C', 'D'}
# Set of terminal symbols
V_T = {'a', 'b', 'c'}
# Set of productions, rules or transitions
P = {
    "S": ["aB"],
    "B": ["bS", "aC", "b"],
    "C": ["bD"],
    "D": ["a", "bC", "cS"],

}
# Initiate the grammar
grammar = Grammar.Grammar(V_N, V_T, P)
# Initiate hte finite automaton
finite_automaton = grammar.to_finite_automaton()
# Create five words
s1 = grammar.generate_string()
s2 = grammar.generate_string()
s3 = grammar.generate_string()
s4 = grammar.generate_string()
s5 = grammar.generate_string()
print(s1 + " " + s2 + " " + s3 + " " + s4 + " " + s5 )
# Verify if words are valid
print("s1 is " + str(finite_automaton.string_belongs_to_language(s1)))
print("s2 is " + str(finite_automaton.string_belongs_to_language(s2)))
print("s3 is " + str(finite_automaton.string_belongs_to_language(s3)))
print("s4 is " + str(finite_automaton.string_belongs_to_language(s4)))
print("s5 is " + str(finite_automaton.string_belongs_to_language(s5)))

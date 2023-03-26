import Lexer

lexer = Lexer.Lexer("2 + 3 * (4 - 1)")
tokens = lexer.tokenize()
print(tokens)


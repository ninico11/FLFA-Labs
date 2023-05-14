import Lexer
import Parser

lexer = Lexer.Lexer("2 + 3 * (4 - 1)")
tokens = lexer.tokenize()
parser = Parser.Parser(tokens)
result = parser.parse()
print(tokens)
print(result)

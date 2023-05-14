# Define the Parser class
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        result = self.expr()
        if self.pos < len(self.tokens):
            raise Exception(f"Invalid syntax: {self.tokens[self.pos][0]}")
        return result

    def expr(self):
        result = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ("Addition", "Subtraction"):
            if self.tokens[self.pos][1] == "Addition":
                self.pos += 1
                result += self.term()
            else:
                self.pos += 1
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ("Multiply", "Divide"):
            if self.tokens[self.pos][1] == "Multiply":
                self.pos += 1
                result *= self.factor()
            else:
                self.pos += 1
                result /= self.factor()
        return result

    def factor(self):
        if self.tokens[self.pos][1] == "Digit":
            result = float(self.tokens[self.pos][0])
            self.pos += 1
            return result
        elif self.tokens[self.pos][1] == "LeftP":
            self.pos += 1
            result = self.expr()
            if self.tokens[self.pos][1] != "RightP":
                raise Exception(f"Missing closing parenthesis")
            self.pos += 1
            return result
        else:
            raise Exception(f"Invalid syntax: {self.tokens[self.pos][0]}")

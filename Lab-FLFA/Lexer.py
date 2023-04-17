import re

Tokens = [
    (r"\s+", None),
    (r"\d+\.\d+|\d+", "Digit"),
    (r"\+", "Addition"),
    (r"-", "Subtraction"),
    (r"\*", "Multiply"),
    (r"/", "Divide"),
    (r"\(", "LeftP"),
    (r"\)", "RightP"),
]

class Lexer:
    def __init__(self, text):
        self.tokens = []
        self.text = text
        self.pos = 0

    def tokenize(self):
        while self.pos < len(self.text):
            match = None
            for pattern, token_type in Tokens:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    if token_type:
                        token = (match.group(), token_type)
                        self.tokens.append(token)
                    break
            if not match:
                raise Exception(f"Invalid token: {self.text[self.pos]}")
            else:
                self.pos = match.end()

        return self.tokens

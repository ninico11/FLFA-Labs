# Topic: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata
### Author: Rotaru Ion 

## Objectives:
  1. Understand what lexical analysis [1] is.
  2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
  3. Implement a sample lexer and show how it works.
## Implementation
```python
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
```
## Conclusion
In this laboratory work I learned and implemented converter from NFA to DFA or from FA to Regular Grammar. 
I learned how to determine if an FA is deterministic or non-deterministic. I found out the steps to convert an NDFA to a DFA
## References
* Kaleidoscope: Kaleidoscope Introduction and the Lexer https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html
* Lexical analysis https://en.wikipedia.org/wiki/Lexical_analysis
                 

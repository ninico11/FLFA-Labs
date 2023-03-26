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
I imported library "re" for regex commonad.
```python
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
```
I implemented this list to tokenize mathematical operations and digits in the "tokenize" method from the "Lexer" class
```python
    def __init__(self, text):
        self.tokens = []
        self.text = text
        self.pos = 0
```
This is a constructor that initialize all the attributes that the "Lexer" class needs to do the tokenization
```python
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
This method realizes the tokenization of the pattern that is given by the user. With the help of the loop, it is checked whether it has reached the end of the expression or not. Then, with the help of the commands from the "re" library, it is checked if the symbol in the expression corresponds to the list of tokens, if so, it is registered in the list, if not, an error appears. And in case the expression is finished, the control operations are finished and the list of tokens and the symbols they correspond to are returned.
## Conclusion
In this laboratory work I learned and implemented lexer for simple mathematical calculations. 
I learned why do we need a lexer and how to tokenize expresion for the parser.
## References
* Kaleidoscope: Kaleidoscope Introduction and the Lexer https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html
* Lexical analysis https://en.wikipedia.org/wiki/Lexical_analysis
                 

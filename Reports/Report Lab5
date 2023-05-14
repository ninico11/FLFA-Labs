# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Rotaru Ion

## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.
## Implementation 
The purpose of the "parse" method is to parse a sequence of tokens and evaluate an expression represented by those tokens.
After evaluating the expression, the code checks if there are any remaining tokens to be processed. If there are, it raises an exception with a message indicating that the syntax is invalid, specifically pointing to the token at the current position (self.tokens[self.pos][0]).
```python
    def parse(self):
        result = self.expr()
        if self.pos < len(self.tokens):
            raise Exception(f"Invalid syntax: {self.tokens[self.pos][0]}")
        return result
```
The purpose of the "expr" method is to parse and evaluate an arithmetic expression.
The method starts by calling another method called "term" to evaluate the first term in the expression.
The "expr" method performs a left-to-right evaluation of an arithmetic expression, taking into account addition and subtraction operations.
```python
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
```
The purpose of the "term" method is same as of the "expr" method but it is used for another arithmetic calculations.
The method begins by calling another method called "factor" to evaluate the first factor in the term.
The term method performs a left-to-right evaluation of a term in an arithmetic expression, taking into account multiplication and division operations.
```python
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
```
The "factor" method handles the parsing and evaluation of factors in an arithmetic expression. Factors can be either numeric values or sub-expressions enclosed within parentheses.
If the token is of type "Digit", it represents a numeric value.
If the token is of type "LeftP", it represents an opening parenthesis. The code increments the position and then recursively calls the expr method to evaluate the expression enclosed within the parentheses.
Next token is of type "RightP" (representing a closing parenthesis). If it is not, an exception is raised indicating a missing closing parenthesis.
If the current token does not match either "Digit" or "LeftP", it indicates an invalid syntax. The code raises an exception with a message indicating the invalid token.
```python
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
```
## Conclusion
In this laboratory work I learned how to implement a parser for a specific grammar. And I lerned about AST concept. 
The AST provides a more abstract and organized representation of the code compared to the raw source code. It simplifies the process of analyzing and manipulating the code during compilation or interpretation
## References
[1] [Parsing Wiki](https://en.wikipedia.org/wiki/Parsing)

[2] [Abstract Syntax Tree Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
                 

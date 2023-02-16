# Topic: Intro to formal languages. Regular grammars. Finite Automata.

### Course: Formal Languages & Finite Automata
### Author: Rotaru Ion 

## Objectives:
1. Understand what a language is and what it needs to have in order to be considered a formal one.

2. Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

    a. Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);

    b. Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;

    c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;

3. According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

    a. Implement a type/class for your grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    
    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;
## Implementation
* Grammar class
    ```python
    import Finite_Automaton


    class Grammar:
        # Constructor of Grammar class
        def __init__(self, V_N, V_T, P):
            self.V_N = V_N
            self.V_T = V_T
            self.P = P

    # Method which generate words corresponding to rules
    def generate_string(self):
        import random
        # Start of the word
        word = "S"
        # Set of final states
        final_state = " "
        # While loop which create a random word
        while word[-1] not in final_state:
            options = []
            for vn, prod in self.P.items():
                if vn == word[-1]:
                    options += prod
            if not options:
                return None
            production = random.choice(options)
            word = word[:-1] + production
        return word

    # Method which transfer from grammar class to finite automaton class
    def to_finite_automaton(self):
        # Initiate finite set of states
        Q = set(self.V_N)
        # Initiate the alphabet
        Sigma = set(self.V_T)
        # Initiate the initial state
        q0 = "S"
        # Initiate the set of final states
        F = "X"
        # Initiate the transition function
        delta = {}
        for vn, prod in self.P.items():
            for symbol in prod:
                if (vn, symbol[0]) in delta :
                    delta[(vn, symbol[0])].append(symbol[1:])
                else:
                    delta[(vn, symbol[0])] = [symbol[1:]]


        # Call the constructor of Finite Automaton class
        return Finite_Automaton.Finite_Automaton(Q, Sigma, delta, q0, F)
    ```

* Finite Automaton Class
    ```python
    class Finite_Automaton:
    # Constructor of Finite_Automaton class
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F
    # Method which check if word is valid
    def string_belongs_to_language(self, input_string):
        # Set the current state to the initial state
        current_state = self.q0
        nr = 0
        # For each symbol in the input string, find the next state using the delta function
        for symbol in input_string:
            if ((current_state[0], symbol) in self.delta) and (nr != len(input_string)-1):
                current_state = self.delta[(current_state[0], symbol)]
            elif nr == len(input_string) - 1:
                if len(current_state) > 1:
                    # If the current state is in the set of final states, return True
                    if current_state[len(current_state)-1] in self.F:
                        return True
                    else:
                        return False
                else:
                    if current_state[0] in self.F:
                        return True
                    else:
                        return False
            nr += 1
    ```
    
## Conclusion
In this laboratory work I learned and implemented regular grammar and a finite automaton. 
I strengthened my knowledge in this field and received new experience in coding. In some moments, errors appeared that were a big obstacle and because of which
I had to review all the code and study new things.
## References
*Regular Expressions, Regular Grammar and Regular Languages: https://www.geeksforgeeks.org/regular-expressions-regular-grammar-and-regular-languages/?ref=lbp
*Deterministic finite automaton: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
*Nondeterministic finite automaton: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
                 


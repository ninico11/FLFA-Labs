# Topic: Chomsky Normal Form

### Course: Formal Languages & Finite Automata
### Author: Rotaru Ion 

## Objectives:
1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.
## ImplementationThis code repeatedly goes through a dictionary's self-contained grammatical rules.P and verifying that no productions in the grammar rules include even one non-terminal symbol. 
This code is looking for any epsilon productions in the grammar, which are production rules that map a non-terminal symbol to an empty string.
For each non-terminal symbol in the grammar, the code first retrieves all the production rules associated with that symbol using 'P[symbol]', which returns a set of strings representing all the possible productions for that non-terminal.
Next, it loops through each of the productions for that non-terminal using 'for production in productions', and checks if the current production is an epsilon production by testing if 'production' is equal to the string 'ε'.
If the current production is an epsilon production, then the code adds the '(symbol, production)' tuple to a list called 'epsilon_productions', indicating that the non-terminal symbol can produce an empty string. It then removes the epsilon production from the set of productions for that non-terminal using 'P[symbol].remove(production)' to ensure that the grammar is in Chomsky normal form, which prohibits epsilon productions.
```python
        epsilon_productions = []
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if production == 'ε':
                    epsilon_productions.append((symbol, production))
                    self.P[symbol].remove(production)
```
This code iterates over each symbol in the grammar and retrieves the set of productions associated with that symbol. For each production, it checks whether the production contains an epsilon string. If it does, the code generates a new production by replacing the epsilon string with an empty string. The new production is then added to the set of productions associated with the same symbol.
```python
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                for epsilon in epsilon_productions:
                    new_production = production.replace(epsilon[0], '')
                    if new_production != production:
                        self.P[symbol].add(new_production)
```
This code repeatedly goes through a dictionary's 'P' and verifying that no productions in the grammar rules include even one non-terminal symbol. 
If such a production is discovered, the code updates the set with the productions of the non-terminal symbol that was discovered in the production and removes the discovered production from the set of productions for that symbol.
```python
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if len(production) == 1 and production.isupper():
                    self.P[symbol].remove(production)
                    self.P[symbol].update(self.P[production])
```
This code is a part of an algorithm used to find the set of all unreachable nonterminals in a context-free grammar.
The algorithm uses a set reachable to keep track of all the nonterminals that are reachable from the start symbol of the grammar.
The while loop keeps iterating until no new nonterminals are added to reachable in an iteration. The changed variable is used to keep track of whether any new nonterminals were added to reachable in the current iteration.
In each iteration, the loop goes through all the nonterminals in the grammar, and for each nonterminal nonterm, it checks whether it is already in reachable. If it is, then it looks at each of its production rules prod, and for each symbol in the production rule, it checks whether it is a nonterminal.
```python
        changed = True
        while changed:
            changed = False
            for nonterm, productions in self.P.items():
                if nonterm in reachable:
                    for prod in productions:
                        for symbol in prod:
                            if symbol in self.V_N:
                                if symbol not in reachable:
                                    reachable.add(symbol)
                                    changed = True
```
This code is used to remove any nonterminal symbols that are not reachable from the starting symbol of the grammar and to remove any productions that can't be reached from the starting symbol.
The code checks for any nonterminal symbols that are not reachable from the starting symbol. It does this by looping through each nonterminal symbol in the 'inaccessible' set and deleting all the productions associated with that symbol from the 'P' dictionary. Then it removes the nonterminal symbol from the 'V_N' set.
Next, the code checks for any productions that can't be reached from the starting symbol. It loops through each nonterminal symbol in the 'P' dictionary and creates a new set of productions that only includes those that have symbols that are either reachable or terminals. It then replaces the original set of productions for that nonterminal symbol with the new set.
```python
        for nonterm in inaccessible:
            del self.P[nonterm]
        self.V_N.remove(nonterm)
        for nonterm, productions in self.P.items():
            new_productions = set()
            for prod in productions:
                if all(symbol in reachable.union(self.V_T) for symbol in prod):
                    new_productions.add(prod)
            self.P[nonterm] = new_productions
```
The code iterates through every symbol in the production rules of the grammar. For each symbol, it checks if any of its productions have more than two symbols. If a production has more than two symbols, the code creates new intermediate symbols to split the production into smaller pieces.
The code generates a new symbol name for each new intermediate symbol that it creates, starting with 'X' followed by an increasing index number. Then, for each symbol in the production that has more than two symbols, the code creates an intermediate symbol and adds it to the production rule. The intermediate symbol will replace that symbol in the production rule.
Finally, the code removes the original production rule with more than two symbols and replaces it with a new production rule that uses the intermediate symbols instead. The resulting grammar will have only two symbols on the right-hand side of each production rule.
```python
        new_symbol_index = 0
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if len(production) > 2:
                    new_symbol = f'X{new_symbol_index}'
                    new_symbol_index += 1
                    self.P[new_symbol] = set()
                    self.P[new_symbol].add(production[0])
                    for i in range(1, len(production) - 1):
                        intermediate_symbol = f'X{new_symbol_index}'
                        new_symbol_index += 1
                        self.P[intermediate_symbol] = set()
                        self.P[intermediate_symbol].add(production[i])
                        self.P[new_symbol].add(intermediate_symbol)
                        self.V_N.add(intermediate_symbol)
                    self.P[new_symbol].add(production[-1])
                    self.P[symbol].remove(production)
                    self.P[symbol].add(new_symbol)
                    self.V_N.add(new_symbol)
```
## Conclusion
In this laboratory work I learned how to obtain Chomsky Normal Form and implemented it in code. 
The laboratory provides a step-by-step interface that allows users to see the process of converting a grammar to Chomsky normal form in real-time, helping us to understand the algorithm and its implementation.
## References
[1] [Chomsky Normal Form Wiki](https://en.wikipedia.org/wiki/Chomsky_normal_form)
                 

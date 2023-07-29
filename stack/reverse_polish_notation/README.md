# Reverse Polish Notation (Medium)
## Description
We are given a valid list which represents a valid expression in reverse polish notation [(link)](https://en.wikipedia.org/wiki/Reverse_Polish_notation) and must compute the value of the expression.

## Runtime
We iterate over all elements $n$ in the list. For each charcter we perform a constant number (1 or 3) of constant time stack operations (push and pop). This gives us a runtime of $\theta(n)$

## Solutions
See python and JavaScript solutions in this directory.

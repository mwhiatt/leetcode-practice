# Valid Palindrome (Easy)
## Description
The problem presented here is simple, given an input string determine if, after cutting out all nonalphanumeric characters and ignoring capitalization, it is a palindrom.

## Runtime
Our run time is pretty trivially $\theta(n)$ in this case. We iterate simultaneously from the back and the front of the cleaned string, checking that the indexes the same distance from the back as the front have the same charcacter. If they do not, we return false.

## Solutions
See Python and Java solutions in this directory.


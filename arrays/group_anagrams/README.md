# Group Anagrams (Medium)
## Description
This problem gives us a list of strings, and asks us to return groups where all the members of each group are valid anagrams of each other.

## Runtime
The runtime our fast solution (in python) is $O(n \cdot k)$ where $n$ is the number of strings we are given and $k$ is the upper bound for the length of any given string. We iterate over all the strings (our $n$ time outer loop), and for each string we iterate over all the characters ($k$ time inner loop) building out a tuple of its character counts to use as a key in the dictionary we create our groups from.

## Solutions
Solution is given in python in this directory.

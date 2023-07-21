# Valid Anagram
## Description
This problem requires us to check whether two inputted strings are valid anagrams of each other, that is, whether or not the have the same characters (and counts of those characters.)

## Runtime
Our fast solutions are $O(n)$ where $n$ is the length of the strings (if they are diffrent lenghts we have a constant time breakout since they can not be anagrams). We define two dictionaries, one for each string, with the characters of each as the keys and the count of each character as the values. We can fill the dictionary values in with one $n$ time iteration over either string. If the dictionaries are not equivalent at the end, we have invalid anagrams. 

## Solutions
See two different solutions in python and c++ in this directory.
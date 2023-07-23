# Contains Duplicate (Easy)
## Description
This simple problem simply requires that we check an array and return false if it is found to have two duplicate entries.
## Runtime
Generally solutions are $O(n)$ where $n$ is the length of the input array. Since we can iterate over the input array and insert elments into a dictionary or hash set with constant time lookup to check if we see them again the future, our run time is $\theta(n)$ if the anagram is valid. 

## Solutions
See solutions in python, java, and c++ in this directory.
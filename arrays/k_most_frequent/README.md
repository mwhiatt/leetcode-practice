# Contains Duplicate (Medium)
## Description
Given an array of integers, and an integer $k$. Return the $k$ most frequent integers in the array.
## Runtime
We make 2 iterations over the array, first counting the occurrences of each integer and storing them in our count dictionary, then storing all the numbers with the same frequency in a list of lists called freqs. Since we index the list of lists by frequency, freqs is in ascending order of frequency. So we iterate from the back of the array, adding the first $k$ elements to the result array before returning it. These 3 $n$ time operations give us a runtime of $O(n)$
## Solutions
See solutions in python and java in this directory.
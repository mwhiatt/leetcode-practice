# Two Sum (Easy)
## Description
Our goal is to find the 2 indices whos values in our input array add up to the specified target value.

## Runtime
We run one for loop over all the $n$ values in the input array. We calculate the difference between the target value and our current value, if that difference has been stored in our dictionary or hashset (constant time lookup,) then we know we have found that pair such that adds to target since. If it is not, we add the (key, value) pair (value, index) into the dictionary for the next iteration.

## Solutions
See Python, C++, and JavaScript solutions in this directory.


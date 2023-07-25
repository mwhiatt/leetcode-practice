# Two Sum II (Sorted Array)
## Description
Same as the Two Sum problem in the arrays section. We want to find two values in the input array that add up to the target value, then return their indices. 

## Runtime
We have a simple $O(n)$ solution using the two pointer method. We start by adding the first and last elements, if that sum is target we are done. If it is not, that sum is either bigger or smaller than target, if it is bigger we decrement our end index to get a smaller result (guaranteed since the array is sorted), and we increment the start index if the current sum is too small. We repeat until we find the proper sum.

## Solutions
See Python and C solutions in this directory.


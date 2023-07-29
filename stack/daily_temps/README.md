# Daily Temperatures (Medium)
## Description
Given an array of integers $temperatures$ where ```temperatures[i]``` represents the tempurate on the ith day. Output an array such that the value at each index $k$ is the amount of days after day $k$ where the temperature is first higher than it was on day $k$, or 0 if that never happens.

## Runtime
We first create an empty stack that will hold the indices of our recently visited days. Then we iterate over the temperatures array, for each temp we iterate backwards over the stack to find the first instance of day with a lower temperature. Then we set the lower day's index in the results array to be our current index minus its index. Then we break and append the current index to the end of the stack. After the loop we return the results array. This single $n$ count iteration with a constant amount of checks in it guarantees us a $O(N)$ run time.


## Solutions
See python and Java solutions in this directory.

# Two Sum (Easy)
## Description
Given an input array $nums$ of size $n$ our goal is to return an array that has at each index, the product of all the values in $nums$ except for that index.

## Runtime
The naive solution would be to have 2 nested for loops where we loop through every value in $nums$ and then loop over the other $n-1$ entries, computing the product and storing it in the result array. This gives a $\theta(n^2)$ runtime. However, we can use a prefix and suffix array to get down to a $\theta(2n + C)$ runtime. We build 2 arrays, $prefix$ and $suffix$, that each contain at index $i$ the product of values up to $i$, and product of values after $i$, respectively. Then the the result value for index $i$ is simply ```prefix[i] * suffix[i]```. 

## Solutions
See Python, JavaScript, and C solutions in this directory.


# Longest Consecutive Group of Integers
## Description
Given an input array $nums$ our goal is to output the longest consecutive streak of integers that can be made from elements in the array in $O(n)$ time.

## Runtime
We first create a set from the array to remove duplicate elements. Then we iterate over all the numbers in the set which is an $O(n)$ operation. For each of these elements, we check if the value immediately below it is in the set, if so it is not the start of a consecutive sequence and we move on. If it is the start of the sequence, we add one to our length tracker variable for every integer that follows the current one. So our solution is $O(nc)$ where $c$ is the length of the longest consecutive sequence, we treat $c$ as constant as LeetCode does and thus our runtime is $O(nc).$

## Solutions
See Python, C++, and JavaScript solutions in this directory.


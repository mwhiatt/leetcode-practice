# Trapped Water (Hard)
## Description
Given an array of integers representing the heights bars spaced 1 unit apart, find the amount of water these bars will trap with the floor.

## Runtime
Our solution is $O(n)$ since we make one dual iteration over the array from the front and back, moving our left pointer in if it is smaller than the biggest wall on the right and vice versa. If we move a pointer in we add the water covered by it to the total.

## Solutions
See Python and Java solutions in this directory.

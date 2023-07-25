# Container With Most Water (Medium)
## Description
Given an array of integers representing the heights of consecutive lines, our goal is to determine the maximum area of water we can hold. That is, with the width of the rectange being the distance in indexes of 2 lines, and the height being the shorter of the 2 lines selected, what is the biggest area rectangle we can build.

## Runtime
Our solution is $O(n)$ since we make one dual iteration over the array from the front and back, checking to see if the current area is bigger than our previous maximum. If the distance between our 2 end values times the maximum height ever drops below the current computed area, we know we can not find any better solution and break.

## Solutions
See Python and C solutions in this directory.

# Car Fleet (Medium)
## Description
We are given three inputs
- $target$: an integer representing the location the cars are traveling
- $positions$: an array of integers where index $i$ represents the position of car $i$, so the ith car's remaining distance is $target-position[i]$
- $speed$: an array of integers where index $i$ represents the speed of car $i$
The cars are driving on a one lane road and thus we must determine how many packs of cars roll across the finish line.

## Runtime
We will use the time each car has left to reach the target as our comparison measure. This is found by using the equation $d = speed[i] \cdot t$ with our earlier equation $d = target-position[i]$, substituting $d$ yields $t = \frac{target-position[i]}{speed[i]}$. Our procedure will be first initialize an empty stack we will use to hold the back car in each pack. Then we will iterate over the cars starting from the highest position (closest) to lowest. This will require a $\theta(n\log n)$ sort. So we add each car to the stack, and pop it off in a subsequent interation if another car catches it before it hits the finish line. Our $\theta(n\log n)$ is our longest operation and thus our run time is $\theta(n\log n)$.

## Solutions
See Python solution in this directory.
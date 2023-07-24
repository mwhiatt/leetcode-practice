# Valid Sudoku (Medium)
## Description
We are given a 2D array of numbers and empty squares (represented by .) and must determine if the board is a valid sudoku suzzle.

## Runtime (Python)
We create 3 dictionaries, one for the rows, one for the columns, and one for the current square (which we index by its (row, col) ordered pair.) We iterate in $\theta(n^2)$ time over all the elements in the board, verifying they do not appear more than once in their row, col, or smaller grid square. If they do not, we add them to the appropriate dictionaries and continue. If they have already appeared, we return $False$. If we reach the end we return $True$ since all squares were valid. 

## Solutions
See Python and Java solutions in this directory.


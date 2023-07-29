# Generate Parentheses (Medium)
## Description
Given an integer $n$ representing the number of pairs of open and close parentheses, generate all valid combinations of those pairs.

## Runtime
We can only add an opening parentheses if our current open count is less than $n$, and only add a closing if our current closing count is less than our open count. So we make 2 recursive calls generating the valid strings in both of these cases. Since there are $2^n$ possible strings ($n$ slots that can either hold a open or close gives $2^n$ by the product rule) we can see our run time is $T(n) = 2T(n-1)$ since we eliminate an uncertain spot with each recursive call. $2T(n-1) \rightarrow O(2^n)$.


## Solutions
See python and Java solutions in this directory.

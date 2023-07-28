# Valid Parentheses (Easy)
## Description
Given an string consisting only of the 6 characters ()[]{} we must determine if the brackets are opened and closed in logical order.

## Runtime
We create a stack to track all the opening brackets we find. We iterate once over the input string, adding each opening bracket to the stack. When we encounter a closing bracket, we check to make sure the stack is not empty, if it is we return false since we have an unopened bracket pair. If it is not empty we verify that the element atop the stack corresponds to the one we are currently checking. If we sucessfully iterate over the string with no errors, we check to make sure the stack is empty (to avoid unclosed brakcets), then return true.

## Solutions
See Python solution in this directory.

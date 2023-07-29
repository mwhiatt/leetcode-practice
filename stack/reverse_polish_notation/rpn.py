import math

class Solution:
    def evalRPN(self, tokens) -> int:
        if not tokens:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for val in tokens:
            if val == '+':
                stack.append(stack.pop() + stack.pop())
            elif val == '-':
                factor = stack.pop()
                stack.append(stack.pop() - factor)
            elif val == '/':
                factor = stack.pop()
                stack.append(math.trunc(stack.pop() / factor))
            elif val == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(val))
        return stack.pop()



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                else:
                    return False
                if char == ')': 
                    if top != '(': return False
                elif char == '}':
                    if top != '{': return False
                else:
                    if top != '[': return False
        return True if not stack else False
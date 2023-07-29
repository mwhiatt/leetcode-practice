class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def recur(oCount, cCount):
            if oCount == cCount == n:
                res.append("".join(stack))

            if oCount < n:
                stack.append('(')
                recur(oCount + 1, cCount)
                stack.pop()
            
            if cCount < oCount:
                stack.append(')')
                recur(oCount, cCount +1)
                stack.pop()
        
        recur(0, 0)
        return res
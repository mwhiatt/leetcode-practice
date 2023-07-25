class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalnum():
                res+=char.lower()
        print(res)
        start = 0
        end = len(res)-1
        while start < end:
            if not res[start] == res[end]:
                return False
            start+=1
            end-=1
        return True

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set() # O(1) lookup vs O(n) for list
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
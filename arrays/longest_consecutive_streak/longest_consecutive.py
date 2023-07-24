class Solution(object):
    def longestConsecutive(self, nums):
        uniques = set(nums)
        longest = 0

        for num in uniques:
            if not (num-1) in uniques:
                length = 1
                while (num+length) in uniques:
                    length+=1
                longest=max(length,longest)
        return longest
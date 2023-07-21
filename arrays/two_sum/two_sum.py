class Solution(object):
    def twoSum(self, nums, target):
        prev = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in prev):
                return [prev[target - nums[i]], i]
            prev[nums[i]] = i
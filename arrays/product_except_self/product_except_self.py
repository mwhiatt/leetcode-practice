class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [0] * (len(nums) - 1) + [1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        prefix = [1]
        res = [suffix[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
            res.append(prefix[i] * suffix[i])

        return res
class Solution:
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and num == nums[i-1]:
                continue # skip duplicate first values
            
            l=i+1
            r=len(nums) - 1
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r-=1
                elif num + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while (nums[l] == nums[l-1] and l<r) :
                        l+=1 # skip duplicate second values
        return res



    
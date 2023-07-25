class Solution:
    def trap(self, height):
        water = 0
        l = 0
        r = len(height) - 1

        lMax, rMax = height[l], height[r]
        while l < r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax, height[l])
                water += lMax - height[l]
            else:
                r-=1
                rMax = max(rMax, height[r])
                water += rMax - height[r]
        return water
        
 
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        h = max(height)
        area = 0

        while l<r:
            area = max(area, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l+=1
            elif height[r] <= height[l]:
                r-=1
            if (r-l) * h <= area:
                break
        return area
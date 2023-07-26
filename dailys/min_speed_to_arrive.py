# July 26, 2023
class Solution:
    def minSpeedOnTime(self, dist, hour):
        speed = -1
        if (hour < len(dist) - 1):
            return speed
        l = 1
        r = 10**10

        while l <= r:
            m = (l + r) // 2
            time=0
            for train in dist[:len(dist)-1]:
                time += math.ceil(train / m)
            time += float(dist[len(dist)-1]) / m
            if (time > hour): 
                l=m+1
            else:
                speed = m
                r = m-1

        return speed
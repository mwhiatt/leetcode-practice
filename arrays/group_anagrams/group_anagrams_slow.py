class Solution(object):
    def isAnagram(self, s, t):
        if (len(s) != len(t)): return False
        sDict, tDict = {}, {}

        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
        return sDict == tDict
    
    def groupAnagrams(self, strs):
        res = []
        while strs:
            current = strs.pop()
            small_list = [current]
            length = len(strs)
            i=0
            while i < length:
                if self.isAnagram(current, strs[i]):
                    small_list.append(strs.pop(i))
                    length-=1
                else:
                    i+=1
            res.append(small_list)
        return res
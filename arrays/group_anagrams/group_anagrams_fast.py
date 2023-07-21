import collections

class Solution(object):
    def groupAnagrams(self, strs):
        res = collections.defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char)-ord('a')]+=1
            res[tuple(counts)].append(word)
        return res.values()

class Solution(object):
    def topKFrequent(self, nums, k):
        freqs = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, val in count.items():
            freqs[val].append(num)

        result = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if (len(result) == k):
                    return result
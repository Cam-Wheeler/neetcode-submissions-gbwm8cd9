from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bins = [[] for _ in range(len(nums))]
        counts = Counter(nums)

        for val, count in counts.items():
            bins[count - 1].append(val)

        res = []
        idx = -1
        while len(res) < k:
            res.extend(bins[idx])
            idx -= 1
        return res[:k]
        
        


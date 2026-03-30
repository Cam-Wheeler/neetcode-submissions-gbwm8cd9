from math import floor
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        bucket_count = max(counts.values())
        buckets = [[] for i in range(bucket_count)]
        for value, count in counts.items():
            buckets[count - 1].append(value)
        print(buckets)

        output = []
        for i in range(1, len(buckets) + 1):
            for j in buckets[-i]:
                output.append(j)
                if len(output) == k:
                    return output
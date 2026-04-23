from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for value, reps in count.items():
            buckets[reps].append(value)
            print(buckets)


        res = []
        for idx in range(len(buckets) -1, -1, -1):
            bucket = buckets[idx]
            for element in bucket:
                res.append(element)
                if len(res) == k:
                    return res
        
            

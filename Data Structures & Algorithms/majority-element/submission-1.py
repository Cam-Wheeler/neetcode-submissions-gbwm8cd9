from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = Counter(nums)
        for val, count in counts.items():
            if count > len(nums) / 2:
                return val

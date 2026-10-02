from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        res = []
        for num, count in counts.items():
            if count > len(nums) // 3:
                res.append(num)

        return res
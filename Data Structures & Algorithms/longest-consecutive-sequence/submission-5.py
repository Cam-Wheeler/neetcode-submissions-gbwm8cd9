class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for idx in range(len(nums)):
            val = nums[idx]
            conseq = 1
            if val - 1 not in nums_set:
                while val + 1 in nums_set:
                    conseq += 1
                    val += 1
                res = max(res, conseq)
        return res
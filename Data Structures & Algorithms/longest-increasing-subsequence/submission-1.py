from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def recurse(idx, prev_idx):
            if idx == len(nums):
                return 0

            key = (idx, prev_idx)
            if key in memo:
                return memo[key]

            exclude = recurse(idx + 1, prev_idx)

            include = 0
            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                include = 1 + recurse(idx + 1, idx)

            memo[key] = max(include, exclude)
            return memo[key]

        return recurse(0, -1)
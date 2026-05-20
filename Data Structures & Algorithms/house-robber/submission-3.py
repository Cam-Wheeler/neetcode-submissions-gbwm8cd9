class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recurse(idx):

            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]
            else:
                memo[idx] = max(nums[idx] + recurse(idx + 2), recurse(idx + 1))
            return memo[idx]
        
        return recurse(0)

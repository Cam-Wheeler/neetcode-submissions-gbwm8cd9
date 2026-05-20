class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recurse(idx):

            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]
            else:
                rob = nums[idx] + recurse(idx + 2)
                not_rob = recurse(idx + 1)
                memo[idx] = max(rob, not_rob)
            return memo[idx]
        
        return recurse(0)

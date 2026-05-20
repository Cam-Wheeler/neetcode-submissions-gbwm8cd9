class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        
        def recurse(idx):

            if idx >= len(nums):
                return 0
            elif idx in memo:
                return memo[idx]
            else:
                steal = recurse(idx + 2)
                not_steal = recurse(idx + 1)
                best = max(nums[idx] + steal, not_steal)
                memo[idx] = best
            
            return memo[idx]

        return recurse(0)
            
            
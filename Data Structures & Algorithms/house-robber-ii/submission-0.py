class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}
        def recurse(idx, flag):
            
            if idx >= len(nums) or flag and idx == len(nums) - 1:
                return 0
            elif (idx, flag) in memo:
                return memo[(idx, flag)]
            else:
                memo[(idx, flag)] = max(nums[idx] + recurse(idx + 2, flag), recurse(idx + 1, flag))
                
            return memo[(idx, flag)]

        return max(recurse(0, True), recurse(1, False))
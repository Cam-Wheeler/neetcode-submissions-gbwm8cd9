class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0

        res = 0
        current_best = float("inf")

        while r < len(nums):
            res += nums[r]
            while res >= target:
                current_best = min(current_best, (r - l) + 1)
                res -= nums[l]
                l += 1
            r += 1
        
        if current_best == float("inf"):
            return 0
        return current_best

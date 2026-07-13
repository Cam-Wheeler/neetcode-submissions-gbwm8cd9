class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}

        def dfs(idx):
            if idx >= len(nums) - 1:
                return 0
            if idx in memo:
                return memo[idx]
            if nums[idx] == 0:
                return float("inf")
            best = float("inf")
            for step in range(1, nums[idx] + 1):
                best = min(best, 1 + dfs(idx + step))
            memo[idx] = best
            return best

        return dfs(0)
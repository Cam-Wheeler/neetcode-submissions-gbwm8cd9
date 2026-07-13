class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}

        def dfs(idx, cnt):

            if idx >= len(nums) - 1:
                return cnt

            if idx in memo:
                return memo[idx]
            
            if nums[idx] == 0:
                return float("inf")
            min_jump = float("inf")
            for i in range(nums[idx], 0, -1):
                min_jump = min(dfs(idx + i, cnt + 1), min_jump)
            memo[idx] = min_jump

            return memo[idx]

        return dfs(0, 0)
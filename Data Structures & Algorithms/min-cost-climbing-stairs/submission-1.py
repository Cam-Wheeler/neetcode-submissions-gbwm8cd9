class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        
        def dfs(idx, flag) -> int:

            if idx >= len(cost):
                return 0

            if (idx, flag) in memo:
                return memo[(idx, flag)]
            
            cost_1 = dfs(idx + 1, flag)
            cost_2 = dfs(idx + 2, flag)

            memo[(idx, flag)] = cost[idx] + min(cost_1, cost_2)
            
            return memo[(idx, flag)]

        first = dfs(0, False)
        second = dfs(1, True)

        return min(first, second)

            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        memo = {}

        res = 0

        def dfs(idx):

            if idx >= len(prices):
                return 0

            if idx in memo:
                return memo[idx]

            l, r = idx, idx
            local_profit = 0
            max_profit = 0
            while r < len(prices):
                if prices[r] - prices[l] > local_profit:
                    local_profit = prices[r] - prices[l]
                    future_gains = dfs(r + 2)
                    max_profit = max(max_profit, local_profit + future_gains)
                if prices[r] < prices[l]:
                    l = r
                r += 1
            memo[idx] = max_profit
            return memo[idx]

        res = dfs(0)

        return res


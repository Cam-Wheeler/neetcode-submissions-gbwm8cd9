class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_holding = prices[0]
        current_profit = 0

        for idx in range(len(prices)):
            current_profit = max(current_profit, prices[idx] - current_holding)
            if prices[idx] < current_holding:
                current_holding = prices[idx]

        return current_profit
            
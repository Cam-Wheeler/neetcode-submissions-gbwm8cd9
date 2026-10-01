class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_holding = prices[0]
        current_profit = 0

        for idx in range(1, len(prices)):
            if prices[idx] > current_holding:
                current_profit += prices[idx] - current_holding
                current_holding = prices[idx]
                continue
            if prices[idx] < current_holding:
                current_holding = prices[idx]

        return current_profit

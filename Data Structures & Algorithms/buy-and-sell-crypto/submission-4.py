class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_buy = prices[0]

        buy, sell = 0, 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
            if prices[sell] < current_buy:
                current_buy = prices[sell]
                buy = sell
            sell += 1
        return max_profit
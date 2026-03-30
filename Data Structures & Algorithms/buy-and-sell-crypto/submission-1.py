class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        final_profit = 0
        for idx in range(1, len(prices), 1):
            if prices[idx] < buy:
                buy = prices[idx]
            profit = prices[idx] - buy
            if profit > final_profit:
                final_profit = profit
        return final_profit

            
            
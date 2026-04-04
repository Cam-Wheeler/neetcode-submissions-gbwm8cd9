class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        head, tail = 0, 0
        current_max_profit = 0

        while tail <= len(prices) - 1:
            trade = prices[tail] - prices[head]
            print(trade)
            current_max_profit = max(current_max_profit, trade)
            if prices[tail] < prices[head]:
                head = tail
            tail += 1
        return current_max_profit
        
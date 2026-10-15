from collections import deque

class StockSpanner:

    def __init__(self):
        self.stocks = deque()
        
    def next(self, price: int) -> int:
        span = 1
        while self.stocks and self.stocks[-1][1] <= price:
            prev_span, _ = self.stocks.pop()
            span += prev_span
        self.stocks.append((span, price))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
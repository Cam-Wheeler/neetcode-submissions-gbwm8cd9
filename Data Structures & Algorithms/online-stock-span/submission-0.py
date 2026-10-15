class StockSpanner:

    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        self.stocks.append(price)
        span = 0
        for idx in range(len(self.stocks) - 1, -1, -1):
            if self.stocks[idx] > price:
                return span
            span += 1
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
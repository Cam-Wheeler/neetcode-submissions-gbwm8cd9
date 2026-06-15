class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
    
        # Step 2: always pop from small and push to large
        val = heapq.heappop_max(self.small)
        heapq.heappush(self.large, val)
    
        # Step 3: rebalance if large is bigger than small
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (self.small[0] + self.large[0]) / 2.0
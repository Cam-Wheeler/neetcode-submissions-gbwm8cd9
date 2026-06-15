import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.counter = 0

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.max_heap, num)
        node = heapq.heappop_max(self.max_heap)
        heapq.heappush(self.min_heap, node)

        if len(self.min_heap) > len(self.max_heap):
            node = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, node)
        
        self.counter += 1

    def findMedian(self) -> float:
        
        if self.counter % 2:
            return self.max_heap[0]
        else:
            return (self.max_heap[0] + self.min_heap[0]) / 2
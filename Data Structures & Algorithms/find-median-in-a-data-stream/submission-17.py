import heapq

class MedianFinder:

    def __init__(self):
        self.left_half = [] # max heap
        self.right_half = [] # min heap

    def addNum(self, num: int) -> None:

        # Push to the correct heap.
        if self.left_half and num < self.left_half[0]:
            heapq.heappush_max(self.left_half, num)
        else:
            heapq.heappush(self.right_half, num)

        # Rebalance if required
        if len(self.left_half) > len(self.right_half) + 1:
            val = heapq.heappop_max(self.left_half)
            heapq.heappush(self.right_half, val)
        
        if len(self.right_half) > len(self.left_half) + 1:
            val = heapq.heappop(self.right_half)
            heapq.heappush_max(self.left_half, val)

        return None
        

    def findMedian(self) -> float:

        if len(self.left_half) > len(self.right_half):
            return self.left_half[0]
        elif len(self.right_half) > len(self.left_half):
            return self.right_half[0]
        else:
            return (self.left_half[0] + self.right_half[0]) / 2
        
        
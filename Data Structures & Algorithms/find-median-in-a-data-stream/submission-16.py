import heapq
class MedianFinder:

    def __init__(self):
        self.first_half = [] # max heap
        self.second_half = [] # min heap

    def addNum(self, num: int) -> None:

        if self.first_half and num < self.first_half[0]:
            heapq.heappush_max(self.first_half, num)
        else:
            heapq.heappush(self.second_half, num)

        # balance if required
        if len(self.first_half) > len(self.second_half) + 1:
                val = heapq.heappop_max(self.first_half)
                heapq.heappush(self.second_half, val)

        if len(self.second_half) > len(self.first_half) + 1:
            val = heapq.heappop(self.second_half)
            heapq.heappush_max(self.first_half, val)

        return None

    def findMedian(self) -> float:

        if len(self.second_half) > len(self.first_half):
            return self.second_half[0]
        elif len(self.first_half) > len(self.second_half):
            return self.first_half[0]
        else:
            return (self.first_half[0] + self.second_half[0]) / 2
        
        
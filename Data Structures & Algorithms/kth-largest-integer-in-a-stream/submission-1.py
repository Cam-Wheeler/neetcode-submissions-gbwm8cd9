import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.heap = []
        for num in nums:
            self.add(num)
                
    def add(self, val: int) -> int:
        if len(self.heap) == self.size:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)
            return self.heap[0]
        else:
            heapq.heappush(self.heap, val)
            return self.heap[0]

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.heap = []
        for value in nums:
            self.add(value)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.capacity:
            heapq.heappop(self.heap)
        return self.heap[0]
        

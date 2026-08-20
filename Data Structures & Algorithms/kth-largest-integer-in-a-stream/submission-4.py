import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        self.k = k

        for num in nums:
            heapq.heappush_max(self.max_heap, num)

    def add(self, val: int) -> int:

        heapq.heappush_max(self.max_heap, val)
        kth_largest = heapq.nlargest(self.k, self.max_heap)
        return kth_largest[-1]

        

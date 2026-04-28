import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            stone1, stone2 = heapq.heappop_max(heap), heapq.heappop_max(heap)
            if stone1 != stone2:
                heapq.heappush_max(heap, abs(stone1 - stone2))
        
        return heap[0] if heap else 0

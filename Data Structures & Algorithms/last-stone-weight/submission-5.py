from _heapq import heappop
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush_max(max_heap, stone)

        while len(max_heap) > 1:
            stone1 = heapq.heappop_max(max_heap)
            stone2 = heapq.heappop_max(max_heap)

            smash = abs(stone1 - stone2)

            if smash:
                heapq.heappush_max(max_heap, smash)
        
        if max_heap:
            return max_heap[0]
        return 0
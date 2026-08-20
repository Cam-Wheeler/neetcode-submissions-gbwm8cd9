import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        x1, y1 = 0, 0
        for idx, coord in enumerate(points):
            x2, y2 = coord[0], coord[1]
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            heapq.heappush(min_heap, (distance, [x2, y2]))
        
        res = []
        for _ in range(k):
            distance, coord = heapq.heappop(min_heap)
            res.append(coord)

        return res
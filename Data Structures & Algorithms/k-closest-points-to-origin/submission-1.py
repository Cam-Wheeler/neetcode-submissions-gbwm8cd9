import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = sqrt((point[0]**2 + point[1]**2))
            heapq.heappush(heap, (distance, point))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res


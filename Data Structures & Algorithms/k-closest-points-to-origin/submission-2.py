import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for idx in range(len(points)):
            distance = sqrt((points[idx][0] - 0)**2 + (points[idx][1] - 0)**2)
            heapq.heappush(min_heap, (distance, idx))

        res = []
        for i in range(k):
            node = heapq.heappop(min_heap)
            res.append(points[node[1]])
        return res
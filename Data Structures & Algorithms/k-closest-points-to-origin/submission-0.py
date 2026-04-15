import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for idx in range(len(points)):
            distance = sqrt((points[idx][0] - 0)**2 + (points[idx][1] - 0)**2)
            distances.append((distance, idx))
        heapq.heapify(distances)
        output = []
        for i in range(k):
            node = heapq.heappop(distances)
            output.append(points[node[1]])
        return output
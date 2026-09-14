import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for idx in range(len(points)):
            for jdx in range(idx + 1, len(points)):
                dist = abs(points[idx][0] - points[jdx][0]) + abs(points[idx][1] - points[jdx][1])
                adj[idx].append((jdx, dist))
                adj[jdx].append((idx, dist))

        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        visited = set()
        cost = 0
        while len(visited) != len(points):

            distance, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            cost += distance

            for neigh_node, neigh_dist in adj[node]:
                if neigh_node not in visited:
                    heapq.heappush(min_heap, (neigh_dist, neigh_node))

        return cost
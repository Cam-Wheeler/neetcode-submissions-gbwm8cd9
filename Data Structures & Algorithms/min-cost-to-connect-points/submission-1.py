class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {node: [] for node in range(n)}

        for i in range(n):
            x_i, y_i = points[i]
            for j in range(i, n):
                x_j, y_j = points[j]
                manhatten = abs(x_i - x_j) + abs(y_i - y_j)
                adj[i].append((manhatten, j))
                adj[j].append((manhatten, i))

        
        # Prims
        visited = set()
        min_heap = [(0, 0)]
        res = 0

        while len(visited) != n:

            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            for nei_cost, nei_node in adj[node]:
                if nei_node not in visited:
                    heapq.heappush(min_heap, (nei_cost, nei_node))
            res += cost

        return res


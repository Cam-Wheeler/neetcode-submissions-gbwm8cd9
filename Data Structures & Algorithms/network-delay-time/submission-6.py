import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {n: [] for n in range(1, n + 1)}

        for src, dest, time in times:
            adj[src].append((dest, time))

        distances = {n: float("inf") for n in range(1, n + 1)}
        distances[k] = 0
        
        min_heap = []
        heapq.heappush(min_heap, (0, k))
        visited = set()

        while min_heap:

            curr_distance, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for neigh_node, neigh_dist in adj[curr_node]:
                new_dist = curr_distance + neigh_dist
                if new_dist < distances[neigh_node] and neigh_node not in visited:
                    distances[neigh_node] = new_dist
                    heapq.heappush(min_heap, (new_dist, neigh_node))
        
        if len(visited) == n:
            return max(distances.values())
        return -1



import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1, 1)}
        for source, target, time in times:
            adj[source].append((target, time))

        distances = {node: float("inf") for node in adj}
        src = k
        distances[k] = 0
        visited = set()
        min_heap = [(0, src)]

        while min_heap:

            current_distance, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbour, time in adj[current_node]:
                new_distance = current_distance + time

                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbour))
        
        if len(visited) != len(distances):
            return -1

        return max(distances.values())

        



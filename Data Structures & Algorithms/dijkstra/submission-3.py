from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = defaultdict(list)
        for source, dest, weight in edges:
            graph[source].append((weight, dest))

        distances = {node: float("inf") for node in range(n)}
        distances[src] = 0
        visited = set()
        min_heap = [(0, src)]

        while min_heap:

            current_distance, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbour_weight, neighbour in graph[current_node]:

                new_distance = current_distance + neighbour_weight
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbour))
        
        for node in distances:
            if node not in visited:
                distances[node] = -1
        
        return distances

        
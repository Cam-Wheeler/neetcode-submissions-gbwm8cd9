import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # adjacency list
        graph = defaultdict(list)
        for source, dest, weight in edges:
            graph[source].append((weight, dest))
        
        # distances 
        distances = {node: float("inf") for node in range(n)}
        distances[src] = 0
        
        # visited
        visited = set()

        # min_heap
        min_heap = [(0, src)] # (distance, node)

        # loop while heap
        while min_heap:

            current_distance, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            for weight, neighbour in graph[current_node]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbour))
        
        for node in distances:
            if node not in visited:
                distances[node] = -1
        
        return distances
                


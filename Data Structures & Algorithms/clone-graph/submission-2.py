from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        visited = set()
        queue = deque()
        graph = {}

        queue.append(node)
        visited.add(node.val)

        while queue:

            old_node = queue.popleft()
            old_val, old_neighbors = old_node.val, old_node.neighbors

            if old_val not in graph:
                new_node = Node(old_val)
                graph[old_val] = new_node
            
            for old_neighbor in old_neighbors:
                if old_neighbor.val not in graph:
                    new_neighbor = Node(old_neighbor.val)
                    graph[old_neighbor.val] = new_neighbor
                    graph[old_val].neighbors.append(new_neighbor)
                else: # Its already in the graph
                    graph[old_val].neighbors.append(graph[old_neighbor.val])
                
                if old_neighbor.val not in visited:
                    queue.append(old_neighbor)
                    visited.add(old_neighbor.val)
        
        return graph[1]







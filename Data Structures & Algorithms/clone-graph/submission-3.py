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

        graph = {}
        graph[node] = Node(node.val)
        queue = deque([node])

        while queue:

            old_node = queue.popleft()

            for old_neighbor in old_node.neighbors:
                if old_neighbor not in graph: # This implicitly filters out nodes that we have already seen. 
                    graph[old_neighbor] = Node(old_neighbor.val)
                    queue.append(old_neighbor)
                graph[old_node].neighbors.append(graph[old_neighbor])
            
        return graph[node]






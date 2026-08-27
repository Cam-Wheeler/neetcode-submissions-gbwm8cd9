"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        visited = set()
        visited.add(node)
        q = deque([node])
        old_new = {}

        while q:
            curr_node = q.popleft()
            
            if curr_node not in old_new:
                old_new[curr_node] = Node(node.val)
            
            node_copy = old_new[curr_node]
            
            for nei in curr_node.neighbors:

                # Create a new version of the neighbour
                if nei not in old_new:
                    old_new[nei] = Node(nei.val)
                node_copy.neighbors.append(old_new[nei])
                    
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)


        return old_new[node]
        



        

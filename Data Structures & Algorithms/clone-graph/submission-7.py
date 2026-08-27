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

        q = deque([node])
        old_new = {}
        old_new[node] = Node(node.val)

        while q:
            curr_node = q.popleft()
            
            for nei in curr_node.neighbors:
                # Create a new version of the neighbour
                if nei not in old_new:
                    old_new[nei] = Node(nei.val)
                    q.append(nei)
                old_new[curr_node].neighbors.append(old_new[nei])

        return old_new[node]
        



        

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        cache = {None: None} # OG Node : New Node

        # Setup cache
        current = head
        while current:

            if current not in cache:
                new_node = Node(current.val)
                cache[current] = new_node
            new_node = cache[current]
            
            # Next setup and wiring
            nxt = current.next
            if nxt not in cache:
                new_nxt = Node(nxt.val)
                cache[nxt] = new_nxt
            new_node.next = cache[nxt]

            # Random setup and wiring
            rnd = current.random
            if rnd not in cache:
                new_rnd = Node(rnd.val)
                cache[rnd] = new_rnd
            new_node.random = cache[rnd]

            current = current.next
        
        return cache[head]

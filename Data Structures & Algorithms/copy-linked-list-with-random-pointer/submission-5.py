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

            if current in cache:
                new_node = cache[current]
            else:
                new_node = Node(current.val)
                cache[current] = new_node
            
            # Next setup and wiring
            nxt = current.next
            if nxt in cache:
                new_node.next = cache[nxt]
            else:
                new_nxt = Node(nxt.val)
                cache[nxt] = new_nxt
                new_node.next = cache[nxt]

            # Random setup and wiring
            rnd = current.random
            if rnd in cache:
                new_node.random = cache[rnd]
            else:
                new_rnd = Node(rnd.val)
                cache[rnd] = new_rnd
                new_node.random = cache[rnd]

            current = current.next
        
        return cache[head]





        # Wiring
        current = head
        while current: # O(n)
            # wire the next pointer
            node = cache[current]
            node.next = cache[current.next]
            # wire the random
            node.random = cache[current.random]
            current = current.next

        return cache[head]

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
            cache[current] = Node(current.val)
            current = current.next


        # Wiring
        current = head
        while current:
            # wire the next pointer
            node = cache[current]
            node.next = cache[current.next]
            # wire the random
            node.random = cache[current.random]
            current = current.next

        return cache[head]

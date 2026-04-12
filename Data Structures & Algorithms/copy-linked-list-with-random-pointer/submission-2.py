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
        
        cache = {None: None}

        current = sentinal = Node(0)
        h2 = head # Needed for second pass
        while head:
            new_node = Node(head.val)
            cache[head] = new_node
            head = head.next
            current.next = new_node
            current = new_node
        
        while h2:
            cache[h2].random = cache[h2.random]
            h2 = h2.next

        return sentinal.next

        
        



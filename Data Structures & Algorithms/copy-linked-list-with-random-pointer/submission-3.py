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
        sentinal = Node(-1)
        current = sentinal
        cache = {None: None}
        head_2 = head

        while head:
            node = Node(head.val)
            cache[head] = node
            current.next = node
            head = head.next
            current = current.next
        
        while head_2:
            cache[head_2].random = cache[head_2.random]
            head_2 = head_2.next
        
        return sentinal.next




        
        



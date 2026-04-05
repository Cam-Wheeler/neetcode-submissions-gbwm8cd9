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
        cache = {}
        cache[None] = None

        sentinal = Node(-100)
        current_old = head
        current_new = sentinal
        while current_old:

            if current_old in cache:
                node = cache[current_old]
            else:
                node = Node(current_old.val)
                cache[current_old] = node
            
            if current_old.random in cache:
                node.random = cache[current_old.random]
            else:
                new_random = Node(current_old.random.val)
                cache[current_old.random] = new_random
                node.random = new_random
            
            current_new.next = node
            current_new = node
            current_old = current_old.next

        current_new.next = None

        return sentinal.next 
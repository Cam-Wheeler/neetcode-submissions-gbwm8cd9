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
        cache = {None: None}

        def getOrCreate(node):
            if node not in cache:
                cache[node] = Node(node.val)
            return cache[node]

        current = head
        while current:
            copy = getOrCreate(current)
            copy.next = getOrCreate(current.next)
            copy.random = getOrCreate(current.random)
            current = current.next

        return cache[head]

        
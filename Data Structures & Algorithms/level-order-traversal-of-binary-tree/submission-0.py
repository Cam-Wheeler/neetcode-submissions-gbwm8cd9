# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        output = [[]]
        queue = deque()
        queue.append((0, root))
        current_level = 0
        while len(queue) > 0:
            level, node = queue.popleft()
            if node:
                if level != current_level:
                    output.append([])
                    current_level += 1
                output[-1].append(node.val)
                queue.append((current_level + 1, node.left))
                queue.append((current_level + 1, node.right))
            
        return output    


            



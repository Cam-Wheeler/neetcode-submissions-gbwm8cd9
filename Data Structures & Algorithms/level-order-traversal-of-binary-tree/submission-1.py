# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        queue = deque()
        queue.append((1, root))
        levels = defaultdict(list)
        while queue:
            level, node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        
        return [x for x in levels.values()]





            



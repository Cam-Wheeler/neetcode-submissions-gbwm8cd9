# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        
        def pre_order_dfs(root, max_seen):

            nonlocal res

            if root is None:
                return
            
            if root.val >= max_seen:
                res += 1
            
            max_seen = max(max_seen, root.val)
            pre_order_dfs(root.left, max_seen)
            pre_order_dfs(root.right, max_seen)

            return
        
        pre_order_dfs(root, -inf)
        return res
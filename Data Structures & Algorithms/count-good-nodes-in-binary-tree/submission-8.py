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
        
        def dfs(node, path_max):
            nonlocal res

            if node is None:
                return

            if node.val >= path_max:
                res += 1
            
            dfs(node.left, max(path_max, node.val))
            dfs(node.right, max(path_max, node.val))

            return

        dfs(root, -101)
        return res
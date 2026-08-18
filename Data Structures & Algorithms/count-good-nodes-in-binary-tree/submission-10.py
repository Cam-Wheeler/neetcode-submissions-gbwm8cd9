# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, path_max):

            if node is None:
                return 0

            res = 0
            if node.val >= path_max:
                res = 1


            path_max = max(path_max, node.val)
            res += dfs(node.left, path_max)
            res += dfs(node.right, path_max)

            return res

        return dfs(root, -101)
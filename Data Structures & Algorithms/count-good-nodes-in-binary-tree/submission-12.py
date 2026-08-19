# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, current_max):

            # base case
            if node is None:
                return 0

            path_max = max(current_max, node.val)

            left = dfs(node.left, path_max)
            right = dfs(node.right, path_max)


            if node.val >= current_max:
                return 1 + left + right

            return left + right

        return dfs(root, -101)
            
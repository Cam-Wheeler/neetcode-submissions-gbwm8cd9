# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        current_max = float("-inf")

        def dfs(node):

            nonlocal current_max

            if node is None:
                return float("-inf")

            left = dfs(node.left)
            right = dfs(node.right)

            best = max(left + node.val, right + node.val, node.val)

            current_max = max(best, left + right + node.val, current_max)

            return best


        dfs(root)
        return current_max
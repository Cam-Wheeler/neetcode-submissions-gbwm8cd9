# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_path = float("-inf")

        def dfs(node):

            nonlocal max_path

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # logic for processing value.
            # left + node, right + node, left + right + node, node
            l_path = left + node.val
            r_path = right + node.val


            max_path = max(l_path, r_path, left + right + node.val, node.val, max_path)

            # logic for passing value up
            pass_up = max(l_path, r_path, node.val, 0)

            return pass_up

        dfs(root)

        return max_path
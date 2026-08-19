# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = float("-inf")

        def dfs(node):
            nonlocal res

            if node is None:
                return float("-inf")

            
            left = dfs(node.left)
            right = dfs(node.right)

            left_path = node.val + left
            right_path = node.val + right
            both_paths = node.val + left + right

            possible_max = max(node.val, left_path, right_path, both_paths)
            res = max(res, possible_max)

            return max(node.val, left_path, right_path)

        dfs(root)
        return res

            
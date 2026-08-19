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

            left_path = left + node.val
            right_path = right + node.val
            both_path = left + right + node.val
            drop_paths = node.val

            best_res = max(left_path, right_path, both_path, drop_paths)

            res = max(res, best_res)

            if best_res == both_path:
                return max(left_path, right_path, drop_paths)

            return best_res

        dfs(root)
        return res

            
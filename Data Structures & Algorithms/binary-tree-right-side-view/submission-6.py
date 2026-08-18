# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        max_seen_level = -1
        res = []

        def dfs(root, level):
            nonlocal res, max_seen_level

            if root is None:
                return

            if root and level > max_seen_level:
                res.append(root.val)
                max_seen_level = max(max_seen_level, level)
            
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        
        dfs(root, 0)
        return res
            

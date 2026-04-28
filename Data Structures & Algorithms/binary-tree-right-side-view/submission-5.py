# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        max_level = -1 
        res = []
        
        def pre_order_dfs(root, level):

            nonlocal max_level, res

            if root is None:
                return

            if level > max_level:
                res.append(root.val)
                max_level = max(max_level, level)
            right = pre_order_dfs(root.right, level + 1)
            left = pre_order_dfs(root.left, level + 1)

            return
        
        pre_order_dfs(root, 0)
        return res
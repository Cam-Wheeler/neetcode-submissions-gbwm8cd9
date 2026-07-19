# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def pre_order_dfs(node, path_max):
            nonlocal res

            if node is None:
                return
            
            if node.val >= path_max:
                res += 1
                path_max = node.val
            
            pre_order_dfs(node.left, path_max)
            pre_order_dfs(node.right, path_max)

            return

        pre_order_dfs(root, root.val)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def pre_order_dfs(node, path_max):

            if node is None:
                return 0
            
            res = 0
            if node.val >= path_max:
                path_max = node.val
                res = 1
            
            res += pre_order_dfs(node.left, path_max)
            res += pre_order_dfs(node.right, path_max)

            return res

        return pre_order_dfs(root, root.val)

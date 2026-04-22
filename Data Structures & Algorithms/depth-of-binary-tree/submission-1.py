# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return self.post_order_trav(root)

    def post_order_trav(self, node):
        
        if node is None:
            return 0
        
        left = self.post_order_trav(node.left)
        right = self.post_order_trav(node.right)

        return max(left, right) + 1
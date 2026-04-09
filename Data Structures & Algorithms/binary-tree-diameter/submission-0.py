# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.current_max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.post_order_trav(root)
        return self.current_max
    
    def post_order_trav(self, root) -> int:

        if root is None:
            return 0
        
        left = self.post_order_trav(root.left)
        right = self.post_order_trav(root.right)

        self.current_max = max(left + right, self.current_max)
        
        return max(left, right) + 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.max_diameter = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        _ = self.post_order_trav(root)

        return self.max_diameter

    def post_order_trav(self,root):
        if root is None:
            return 0
        
        left = self.post_order_trav(root.left)
        right = self.post_order_trav(root.right)

        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left, right)
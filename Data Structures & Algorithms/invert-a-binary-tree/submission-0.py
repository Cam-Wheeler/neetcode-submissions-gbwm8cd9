# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return 
        
        left = self.post_order_trav(root.left)
        right = self.post_order_trav(root.right)

        root.left = right
        root.right = left

        return root


    def post_order_trav(self, node):
        if node is None:
            return node

        left = self.post_order_trav(node.left)
        right = self.post_order_trav(node.right)
        node.left = right
        node.right = left

        return node

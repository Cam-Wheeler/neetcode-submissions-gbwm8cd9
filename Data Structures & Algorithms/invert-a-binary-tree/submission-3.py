# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None
        
        self.post_order_trav(root)

        return root
    
    def post_order_trav(self, node):

        if node is None:
            return
        
        self.post_order_trav(node.left)
        self.post_order_trav(node.right)
        tmp = node.left
        node.left = node.right
        node.right = tmp

        return
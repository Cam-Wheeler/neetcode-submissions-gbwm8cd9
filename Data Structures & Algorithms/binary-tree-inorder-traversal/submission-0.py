# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.in_order_trav(root)
        return self.result
    
    def in_order_trav(self, root):
        if root is None:
            return
        
        left = self.in_order_trav(root.left)

        self.result.append(root.val)

        right = self.in_order_trav(root.right)

        return
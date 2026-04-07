# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.values = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root is None:
            return
        
        self.in_order_trav(root)

        return self.values[k - 1]
    
    def in_order_trav(self, root) -> None:

        if root is None:
            return

        if root.left:
            self.in_order_trav(root.left)
        
        self.values.append(root.val)

        if root.right:
            self.in_order_trav(root.right)

        return

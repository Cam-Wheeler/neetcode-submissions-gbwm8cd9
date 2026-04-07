# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.count = None
        self.result = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = k
        self.result = root.val

        if root is None:
            return

        self.in_order_trav(root)

        return self.result
    
    def in_order_trav(self, root: Optional[TreeNode]):

        if root is None:
            return
        
        self.in_order_trav(root.left)
        self.count -= 1
        if self.count == 0:
            self.result = root.val
            return
        self.in_order_trav(root.right)




        


        

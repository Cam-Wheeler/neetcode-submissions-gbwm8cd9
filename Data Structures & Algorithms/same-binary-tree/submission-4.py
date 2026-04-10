# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.is_same = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if p and not q or not p and q:
            return False

        self.in_order_trav(p, q)

        return self.is_same
        
    
    def in_order_trav(self, p, q):

        if not p and not q:
            return

        if p and not q or not p and q:
            self.is_same = False
            return

        if p.val == q.val:
            self.in_order_trav(p.left, q.left)
            self.in_order_trav(p.right, q.right)
        
        if p.val != q.val:
            self.is_same = False
        
        return
        
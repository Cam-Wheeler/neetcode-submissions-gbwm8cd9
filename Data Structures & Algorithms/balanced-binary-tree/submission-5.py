# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def post_order_trav(root):
            if root is None:
                return 0
            
            left = post_order_trav(root.left)
            right = post_order_trav(root.right)

            print(abs(left - right))
            if abs(left - right) > 1:
                self.balanced = False
            
            return max(left, right) + 1
        
        post_order_trav(root)
        return self.balanced
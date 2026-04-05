# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lb = -inf
        ub = inf

        return self.isValid(root, lb, ub)

    def isValid(self, node, lb, ub) -> bool:

        if node is None:
            return True
        
        if node.val > lb and node.val < ub:
            return (self.isValid(node.left, lb, node.val) and
                    self.isValid(node.right, node.val, ub))
        else:
            return False
            
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot is None: # If subRoot is None, we can always find it on the leaf nodes
            return True

        if root is None: # Subroot must be present and root is None
            return False

        if self.check_subtree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    
    def check_subtree(self, node, subRoot):

        if node is None and subRoot is None: # Both are none
            return True

        if (node and not subRoot) or (not node and subRoot): # One is none and the other isnt
            return False

        if node.val == subRoot.val:
            return (self.check_subtree(node.left, subRoot.left) 
                    and 
                    self.check_subtree(node.right, subRoot.right))

        return False
        


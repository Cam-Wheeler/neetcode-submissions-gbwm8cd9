# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
        

    def isSameTree(self, node: TreeNode, subRoot: TreeNode) -> bool:
        
        if node is None and subRoot is None:
            return True

        if node and subRoot and node.val == subRoot.val:
            return (self.isSameTree(node.left, subRoot.left) and 
                    self.isSameTree(node.right, subRoot.right))

        return False
        


            

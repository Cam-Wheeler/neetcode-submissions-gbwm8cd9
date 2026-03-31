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
        
        if self.same_tree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def same_tree(self, node, subRoot) -> bool:
        """Given a node, checks if the subtree can be build from the subnodes of that node"""
        if node is None and subRoot is None:
            return True
        
        if node and subRoot and node.val == subRoot.val:
            return (self.same_tree(node.left, subRoot.left) and
                    self.same_tree(node.right, subRoot.right))
        
        return False
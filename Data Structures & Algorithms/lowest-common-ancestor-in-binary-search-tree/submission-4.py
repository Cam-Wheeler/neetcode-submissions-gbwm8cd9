# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root is None:
            return None
        
        if (root.val <= q.val and root.val >= p.val) or (root.val <= p.val and root.val >= q.val): # We have our split.
            return root

        if (root.val > q.val and root.val > p.val): # if the value at the current node is greater, explore left
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q) # the value must be smaller, explore right
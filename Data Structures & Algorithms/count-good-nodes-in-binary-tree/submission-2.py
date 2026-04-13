# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.result = 0

    def goodNodes(self, root: TreeNode) -> int:
        
        self.pre_order_trav(root, -math.inf)

        print(self.result)
        return self.result

    
    def pre_order_trav(self, root, current_max):
        if root is None:
            return
        
        if root.val >= current_max:
            self.result += 1
        
        self.pre_order_trav(root.left, max(root.val, current_max))
        self.pre_order_trav(root.right, max(root.val, current_max))

        return
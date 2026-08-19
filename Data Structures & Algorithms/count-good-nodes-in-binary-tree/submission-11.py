# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def pre_order(node, current_max):

            nonlocal res

            # base case
            if node is None:
                return None


            if node.val >= current_max:
                current_max = max(current_max, node.val)
                res += 1

            pre_order(node.left, current_max)
            pre_order(node.right, current_max)

            return None

        pre_order(root, -101)
        return res
            
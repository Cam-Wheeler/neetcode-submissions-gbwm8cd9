# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = None
        
        def iot(node):
            nonlocal cnt, res

            if node is None or res is not None:
                return
            
            iot(node.left)
            cnt += 1
            if cnt == k:
                res = node.val

            iot(node.right)

            return
        
        iot(root)
        return res
            

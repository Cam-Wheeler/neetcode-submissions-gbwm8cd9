# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def recurse(l, r):
            nonlocal pre_idx

            if l > r:
                return None
            
            root_value = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_value)
            mid = indices[root_value]
            root.left = recurse(l, mid - 1)
            root.right = recurse(mid + 1, r)
            return root

        return recurse(0, len(inorder) - 1)

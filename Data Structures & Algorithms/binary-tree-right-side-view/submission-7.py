# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        max_height_seen = -1
        def dfs(node, height):
            nonlocal max_height_seen, res

            if node is None:
                return
            
            if height > max_height_seen:
                res.append(node.val)
                max_height_seen = height
            
            dfs(node.right, height + 1)
            dfs(node.left, height + 1)

            return
        dfs(root, 0)
        
        return res
            



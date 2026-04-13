# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.right_depth = 0
        self.output = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        self.process(root, 1)
        self.process(root.left, 2)

        return self.output

    def process(self, root, depth):
        if root is None:
            return

        if root and depth > self.right_depth:
            self.output.append(root.val)
            self.right_depth = depth
        
        self.process(root.right, depth + 1)
        self.process(root.left, depth + 1)

        return


        


        

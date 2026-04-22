# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if (not p and q) or (not q and p):
            return False

        p_q = deque([p])
        q_q = deque([q])

        while p_q and q_q:
            p_node = p_q.pop()
            q_node = q_q.pop()

            if p_node and q_node and (p_node.val != q_node.val):
                return False
            elif p_node and not q_node or q_node and not p_node:
                return False
            elif not p_node and not q_node:
                continue
            else:
                p_q.append(p_node.left)
                p_q.append(p_node.right)
                q_q.append(q_node.left)
                q_q.append(q_node.right)
        return True 



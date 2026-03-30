# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p_queue = deque()
        q_queue = deque()

        if p and q:
            p_queue.append(p)
            q_queue.append(q)
        elif not p and not q:
            return True
        else:
            return False
        
        while len(p_queue) > 0 or len(q_queue) > 0:

            if len(p_queue) != len(q_queue):
                return False
            
            p_node = p_queue.pop()
            print(p_node)
            q_node = q_queue.pop()
            print(q_node)

            # Handle None
            if p_node == None and q_node == None:
                continue
            elif (p_node == None and q_node != None) or (q_node == None and p_node != None):
                return False
            # Handle nodes
            elif p_node.val == q_node.val:
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)
            else:
                return False
        
        return True


        
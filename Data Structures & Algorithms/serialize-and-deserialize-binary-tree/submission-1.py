# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ""

        # Level order trav for the encoding, treating Nones as "N"
        q = deque()
        q.append(root)
        encoding = []

        while q:
            node = q.popleft()
            if node is None:
                encoding.append("N")
            else:
                q.append(node.left)
                q.append(node.right)
                encoding.append(str(node.val))
        
        return ",".join(encoding)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if data == "":
            return None

        split_chars = data.split(",")

        q = deque()
        root = TreeNode(val=int(split_chars[0]))
        q.append(root)
        index = 1

        while q:

            current = q.popleft()
            
            # Deal with the left.
            left_val = split_chars[index]
            if left_val == "N":
                current.left = None
            else:
                left_node = TreeNode(int(left_val))
                current.left = left_node
                q.append(left_node)
            index +=1 
            
            right_val = split_chars[index]
            if right_val == "N":
                current.right = None
            else:
                right_node = TreeNode(int(right_val))
                current.right = right_node
                q.append(right_node)
            index += 1

        return root



            

    










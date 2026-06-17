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
        encoding = ""

        while q:
            node = q.popleft()
            if node is None:
                encoding += "#1N"
            else:
                int_str = str(node.val)
                encoding += f"#{len(int_str)}{int_str}"
                q.append(node.left)
                q.append(node.right)
        return encoding
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if data == "":
            return None

        q = deque()
        idx, value = self.collect_value(0, data)
        print(idx)
        root = TreeNode(val=value)
        q.append(root)

        while q:
            current = q.popleft()
            idx, left_val = self.collect_value(idx, data)
            idx, right_val = self.collect_value(idx, data)
            if left_val:
                left_node = TreeNode(val=left_val)
                current.left = left_node
                q.append(left_node)
            else:
                current.left = left_val # its None
            
            if right_val:
                right_node = TreeNode(val=right_val)
                current.right = right_node
                q.append(right_node)
            else:
                current.right = right_val # its None
        return root

    def collect_value(self, idx, data):
        
        skip = int(data[idx + 1])
        value = data[idx + 2: idx + 2 + skip]
        if value == "N":
            return idx + 2 + skip, None
        else:
            return idx + 2 + skip, int(value)

            

    










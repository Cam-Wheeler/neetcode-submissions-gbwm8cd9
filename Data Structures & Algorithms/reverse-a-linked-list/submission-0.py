# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None

        current_node = head
        prev = None
        while current_node:
            temp = current_node.next
            current_node.next = prev
            if temp == None:
                head = current_node
                break
            else:
                prev = current_node
                current_node = temp
        
        return head
        
         
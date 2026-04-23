# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        current = sentinal = ListNode()
        current.next = head
        while current.next:
            if head.val == val:
                tmp = head.next
                current.next = tmp
                head.next = None
                head = tmp
            else:
                head = head.next
                current = current.next
        
        return sentinal.next
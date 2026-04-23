# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head.next is None:
            return
        
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        tail = slow.next
        prev = slow.next = None
        while tail:
            tmp = tail.next
            tail.next = prev
            prev = tail
            tail = tmp
        
        c1 = head
        c2 = prev

        while c2:
            tmp1 = c1.next
            tmp2 = c2.next
            c1.next = c2
            c2.next = tmp1
            c1 = tmp1
            c2 = tmp2
    

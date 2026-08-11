# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        nth = head
        fast = head
        for i in range(n):
            fast = fast.next
        
        prev = None
        while fast:
            prev = nth
            nth = nth.next
            fast = fast.next

        if prev:
            prev.next = nth.next
            nth.next = None
            return head
        else:
            new_head = head.next
            nth.next = None
            return new_head


        
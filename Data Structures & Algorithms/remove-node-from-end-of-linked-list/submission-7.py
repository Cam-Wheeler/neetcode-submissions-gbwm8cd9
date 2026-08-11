# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        cnt = 0
        start = head
        while start:
            start = start.next
            cnt += 1
        
        nth = cnt - n
        prev = None
        curr = head
        for i in range(nth):
            prev = curr
            curr = curr.next

        if prev:
            prev.next = curr.next
            curr.next = None
            return head
        else:
            new_head = head.next
            curr.next = None
            return new_head


        
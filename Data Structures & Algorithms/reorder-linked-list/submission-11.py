# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        sentinal = head
        f, s = sentinal.next, sentinal
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # Reverse the 2nd half
        prev = None
        curr = s.next
        s.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Merge
        c1 = sentinal
        c2 = prev
        while c2:
            tmp1, tmp2 = c1.next, c2.next
            c1.next = c2
            c2.next = tmp1
            c1, c2 = tmp1, tmp2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse
        end = slow.next
        slow.next = prev = None
        while end:
            tmp = end.next
            end.next = prev
            prev = end
            end = tmp

        h1 = head
        h2 = prev
        while h2:
            tmp1 = h1.next
            tmp2 = h2.next
            h1.next = h2
            h2.next = tmp1
            h1 = tmp1
            h2 = tmp2
        






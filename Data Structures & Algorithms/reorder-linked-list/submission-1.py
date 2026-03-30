# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Should handle 1 and 2 nodes only.
        if head.next is None or head.next.next is None: # short circuits
            return
            
        # Setup for fast and slow.
        slow = head
        fast = head
        while fast and fast.next : # short circuits
            slow = slow.next
            fast = fast.next.next

        # Now that we have our fast and slow in position, lets start to turn the second half around. 
        prev = slow
        current = prev.next 
        prev.next = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        reversed_head = prev # At the end, prev will be the last node, current will be None do we do not want that. 

        # Now we need to do the integration of the two lists. 
        current = head
        while reversed_head.next:
            tmp = current.next
            current.next = reversed_head
            reversed_head = reversed_head.next
            current.next.next = tmp
            current = tmp

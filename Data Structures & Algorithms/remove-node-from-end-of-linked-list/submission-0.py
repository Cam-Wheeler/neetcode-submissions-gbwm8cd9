# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinal = head
        fast = head
        slow = head

        # Move fast up.
        for i in range(1, n):
            fast = fast.next
        
        # Check if we are moving sential. 
        if fast.next == None:
            tmp = sentinal
            sentinal = sentinal.next
            tmp.next = None # Orphans start.
            return sentinal

        # We are now removing a node in the middle or end somewhere.
        prev = None
        while fast.next != None:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next
        slow.next = None # Orphans the node we are removing. 
        return sentinal
        
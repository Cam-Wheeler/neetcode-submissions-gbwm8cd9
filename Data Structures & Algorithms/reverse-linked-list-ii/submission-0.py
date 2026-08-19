# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy
        
        for _ in range(left):
            slow_p = slow
            slow = slow.next

        for _ in range(right):
            fast = fast.next

        fast_n = fast.next

        # Flip
        prev = fast_n
        while slow != fast_n:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        slow_p.next = fast

        return dummy.next


        


        

        

        

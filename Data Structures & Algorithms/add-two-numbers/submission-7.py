# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # our linked list
        sentinal = ListNode()
        current = sentinal

        # track the overflow
        overflow = 0

        while l1 or l2:
            # Could be None
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            val = l1_val + l2_val
            val += overflow

            # compute if there is still overflow.
            overflow = val // 10
            if overflow:
                val = val % 10

            current.next = ListNode(val=val)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Handle remaining overflow if its present.
        if overflow:
            current.next = ListNode(overflow)

        return sentinal.next
        


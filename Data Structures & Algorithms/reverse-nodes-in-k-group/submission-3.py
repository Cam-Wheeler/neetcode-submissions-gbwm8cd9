# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(-1, head)
        prev_group = dummy

        while True:

            kth = self.get_kth(prev_group, k)
            if kth is None:
                break
            next_group = kth.next
            
            # reverse
            prev, curr = kth.next, prev_group.next
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Link groups
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        return dummy.next
    
    def get_kth(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


    
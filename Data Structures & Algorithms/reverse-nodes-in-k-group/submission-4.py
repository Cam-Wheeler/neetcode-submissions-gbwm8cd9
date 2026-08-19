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
        group_prev = dummy


        while True:

            kth = self.get_kth(group_prev, k)
            if not kth:
                break

            group_start = kth.next

            # reversal
            prev, curr = kth.next, group_prev.next
            while curr != group_start:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # linking
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def get_kth(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -=1

        return curr
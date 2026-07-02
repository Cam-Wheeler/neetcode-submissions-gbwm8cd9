
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        sentinel = ListNode(0, head)
        groupPrev = sentinel

        while True:

            kth = self.get_kth_node(groupPrev, k)
            if kth is None:
                break
            groupNext = kth.next
            prev, current = kth.next, groupPrev.next
            while current != groupNext:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return sentinel.next
    
    def get_kth_node(self, current, k):

        while current and k > 0:
            current = current.next
            k -= 1
        
        return current
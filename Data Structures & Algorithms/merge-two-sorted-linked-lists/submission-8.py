# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        start = ListNode()
        sentinel = start

        c1, c2 = list1, list2

        while c1 and c2:

            if c1.val <= c2.val:
                start.next = c1
                start = c1
                c1 = c1.next
            else:
                start.next = c2
                start = c2
                c2 = c2.next
        
        if c1 is None:
            start.next = c2
        elif c2 is None:
            start.next = c1

        return sentinel.next
            
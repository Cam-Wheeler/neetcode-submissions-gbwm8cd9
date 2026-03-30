# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return None

        prev = ListNode()
        head = prev
        l1 = list1
        l2 = list2
        
        while l1 and l2:
            if l1.val >= l2.val:
                prev.next = l2
                prev = l2
                l2 = l2.next
            else:
                prev.next = l1
                prev = l1
                l1 = l1.next
        
        if l1 == None:
            prev.next = l2
        else:
            prev.next = l1
        
        return head.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        cycle = False

        while fast != None:
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            slow = slow.next
            if fast == slow:
                cycle = True
                break
        
        return cycle

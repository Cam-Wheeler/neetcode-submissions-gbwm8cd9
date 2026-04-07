# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head.next == None or head.next.next == None:
            return

        current = head
        while current.next.next != None:
            last = current.next
            prev = current
            tmp = current.next
            # Take us to the end.
            while last.next != None:
                prev = last
                last = last.next
            if prev == current:
                break
            # Swap
            current.next = last
            last.next = tmp
            prev.next = None
            current = tmp
            if current.next == None:
                break
        return 


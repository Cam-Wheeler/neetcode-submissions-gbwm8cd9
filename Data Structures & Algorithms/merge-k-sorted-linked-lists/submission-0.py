# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        heap = []
        i = 0
        for head in lists:
            while head != None:
                heapq.heappush(heap, (head.val, i, head))
                head = head.next
                i += 1
        
        sentinal = ListNode()
        prev = sentinal

        while heap:
            _, _, node = heapq.heappop(heap)
            node.next = None
            prev.next = node
            prev = node
        
        return sentinal.next

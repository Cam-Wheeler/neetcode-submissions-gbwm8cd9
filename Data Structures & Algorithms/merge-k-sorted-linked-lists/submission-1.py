# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        sentinal = ListNode()
        prev = sentinal

        while heap:
            val, i, node = heapq.heappop(heap)
            prev.next = node
            prev = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return sentinal.next
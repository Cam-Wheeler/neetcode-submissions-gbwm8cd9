# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None

        min_heap = []

        # init the min heap.
        for idx in range(len(lists)):
            if lists[idx] is not None:
                head = lists[idx]
                heapq.heappush(min_heap, (head.val, idx, head))


        current = ListNode()
        sentinal = current
        while min_heap:
            val, k, node = heapq.heappop(min_heap)
            current.next = node
            current = node
            # Now we need to add the next node. We are not adding None. Heap will empty when at the end.
            node_to_add = node.next
            if node_to_add:
                heapq.heappush(min_heap, (node_to_add.val, k, node_to_add))
        
        return sentinal.next
            

        
        

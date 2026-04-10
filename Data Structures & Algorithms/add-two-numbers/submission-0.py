# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = 0
        multiple1 = 1
        while l1:
            val1 += l1.val * multiple1
            multiple1 *= 10
            l1 = l1.next
        
        val2 = 0
        multiple2 = 1
        while l2:
            val2 += l2.val * multiple2
            multiple2 *= 10
            l2 = l2.next
        
        total = str(val1 + val2)

        node = sentinal = ListNode(0)
        for idx in range(len(total) - 1, -1, -1):
            new_node = ListNode(total[idx])
            node.next = new_node
            node = new_node

        return sentinal.next






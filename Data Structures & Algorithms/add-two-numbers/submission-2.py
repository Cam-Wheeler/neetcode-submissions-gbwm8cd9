# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        multiple = 1
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val += (l1_val + l2_val) * multiple
            multiple *= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        total = str(val)

        node = sentinal = ListNode(0)
        for idx in range(len(total) - 1, -1, -1):
            new_node = ListNode(total[idx])
            node.next = new_node
            node = new_node

        return sentinal.next






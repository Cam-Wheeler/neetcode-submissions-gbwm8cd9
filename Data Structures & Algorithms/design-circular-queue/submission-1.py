class DLLNode(object):

    def __init__(self, value, nxt, prev) -> None:
        self.value = value
        self.nxt = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = DLLNode(-1, None, None)
        self.tail = DLLNode(-1, None, None)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # Sort out cur pointers
        cur = DLLNode(value, None, None)
        cur.prev = self.tail.prev
        cur.nxt = self.tail

        # join it in
        self.tail.prev.nxt = cur
        self.tail.prev = cur
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head.nxt = self.head.nxt.nxt
        self.head.nxt.prev = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.nxt.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.value
        

    def isEmpty(self) -> bool:
        if self.head.nxt == self.tail:
            return True
        return False        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
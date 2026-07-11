class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.start = 0
        self.rear = 0        

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] == -1:
            self.queue[self.rear] = value
            self.rear += 1
            if self.rear == len(self.queue):
                self.rear = 0
            return True
        return False
        
    def deQueue(self) -> bool:
        if self.queue[self.start] == -1:
            return False
        self.queue[self.start] = -1
        self.start += 1
        if self.start == len(self.queue):
            self.start = 0
        return True
        
    def Front(self) -> int:
        return self.queue[self.start]
        
    def Rear(self) -> int:
        return self.queue[self.rear - 1]
        
    def isEmpty(self) -> bool:
        if self.start == self.rear and self.queue[self.start] == -1:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.start == self.rear and self.queue[self.rear] != -1:
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
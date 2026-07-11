from collections import deque

class MyQueue:

    def __init__(self):
        self.active = deque()
        self.passive = deque()
        

    def push(self, x: int) -> None:
        self.active.append(x)
        
    def pop(self) -> int:
        return self.move_back_and_forward(pop=True)
        

    def peek(self) -> int:
        return self.move_back_and_forward(pop=False)

    def empty(self) -> bool:
        if self.active:
            return False
        return True
    
    def move_back_and_forward(self, pop: bool):
        for _ in range(len(self.active)):
            self.passive.append(self.active.pop())
        
        if pop:
            res = self.passive.pop()
        else:
            res = self.passive[-1]

        for _ in range(len(self.passive)):
            self.active.append(self.passive.pop())
        
        return res

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_val = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val or self.min_val[-1] >= val:
            self.min_val.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_val[-1]:
            self.min_val.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
        

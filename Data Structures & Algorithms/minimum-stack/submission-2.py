from collections import deque
from math import inf

class MinStack:

    def __init__(self):
        self.min_val = inf
        self.main_stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.main_stack.pop()
        if val == self.min_stack[-1]:
            _ = self.min_stack.pop()
        return val
        
        
    def top(self) -> int:
        return self.main_stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
        

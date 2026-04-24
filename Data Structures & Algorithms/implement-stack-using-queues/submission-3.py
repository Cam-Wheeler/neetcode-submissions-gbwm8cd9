from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.active = self.q1
        self.follower = self.q2

    def push(self, x: int) -> None:
        self.active.append(x)

    def pop(self) -> int:
        for _ in range(len(self.active)):
            value = self.active.popleft()
            if len(self.active) == 0:
                res = value
            else:
                self.follower.append(value)

        tmp = self.follower
        self.follower = self.active
        self.active = tmp
        return res

            
    def top(self) -> int:
        if self.q1:
            return self.q1[-1]
        if self.q2:
            return self.q2[-1]

    def empty(self) -> bool:
        if not self.q1 and not self.q2:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

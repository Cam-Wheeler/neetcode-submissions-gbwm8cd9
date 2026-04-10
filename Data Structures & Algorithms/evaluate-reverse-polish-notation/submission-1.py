from collections import deque

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations_map = {"*": lambda x, y: x * y,
                          "/": lambda x, y: int(x / y),
                          "+": lambda x, y: x + y,
                          "-": lambda x, y: x - y}

        for token in tokens:
            if token in operations_map:
                y = stack.pop()
                x = stack.pop()
                stack.append(operations_map[token](x, y))
            else:
                stack.append(int(token))

        return stack.pop()
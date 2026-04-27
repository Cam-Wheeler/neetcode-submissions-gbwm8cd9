from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            node = (idx, temp)
            while stack and stack[-1][1] < node[1]:
                popped = stack.pop()
                res[popped[0]] = node[0] - popped[0]
            stack.append(node)
        return res
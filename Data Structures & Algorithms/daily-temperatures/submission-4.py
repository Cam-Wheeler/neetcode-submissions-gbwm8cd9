from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()

        for idx, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                node = stack.pop()
                result[node[0]] = idx - node[0]
            stack.append((idx, val))

        return result
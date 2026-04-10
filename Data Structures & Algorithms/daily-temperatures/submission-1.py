from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        output = [0] * len(temperatures)
        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > stack[-1][1]:
                old_idx, temperature = stack.pop()
                output[old_idx] = idx - old_idx
            stack.append((idx, temperatures[idx]))

        return output

                    
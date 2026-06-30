from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = deque()

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                index, prev_height = stack.pop()
                res = max(res, prev_height * (idx - index))
                start = index
            stack.append((start, height))

        for idx, height in stack:
            res = max(res, height * (len(heights) - idx))
        
        return res



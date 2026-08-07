from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        stack = deque()

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                prev_idx, prev_height = stack.pop()
                max_rect = max(max_rect, (idx - prev_idx) * prev_height)
                start = prev_idx
            stack.append((start, height))

        for idx, height in stack:
            max_rect = max((len(heights) - idx) * height, max_rect)
        
        return max_rect
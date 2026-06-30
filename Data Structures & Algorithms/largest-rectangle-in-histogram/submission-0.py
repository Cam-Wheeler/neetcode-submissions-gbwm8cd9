class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            min_seen = heights[i]
            width = 1
            for j in range(i, len(heights), 1):
                min_seen = min(heights[j], min_seen)
                res = max(min_seen * width, res)
                width += 1
        
        return res


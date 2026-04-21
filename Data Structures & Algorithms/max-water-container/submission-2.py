class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        head = 0
        tail = len(heights) - 1

        while head < tail:
            water = (tail - head) * min(heights[head], heights[tail])
            current_max = max(current_max, water)
            if heights[head] < heights[tail]:
                head += 1
            else:
                tail -= 1 # works for draws on height as well. 
        
        return current_max
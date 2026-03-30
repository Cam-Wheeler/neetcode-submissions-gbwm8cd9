class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        head = 0
        tail = len(heights) - 1
        while head < tail:
            min_side = min(heights[head], heights[tail])
            print(min_side)
            water = min_side * (tail - head)
            if water > max_water:
                max_water = water
            if heights[head] > heights[tail]:
                tail -= 1
            elif heights[tail] > heights[head]:
                head += 1
            else:
                head += 1
        return max_water
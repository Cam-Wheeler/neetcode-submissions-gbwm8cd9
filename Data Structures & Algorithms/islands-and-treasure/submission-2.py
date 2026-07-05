from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))
        
        def add_square(r, c):

            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            queue.append((r, c))

        level = 0
        while queue:
            for i in range(len(queue)): # Iterate through the queue for that level.
                row, col = queue.popleft()
                grid[row][col] = level
                add_square(row + 1, col)
                add_square(row - 1, col)
                add_square(row, col + 1)
                add_square(row, col - 1)
            level += 1








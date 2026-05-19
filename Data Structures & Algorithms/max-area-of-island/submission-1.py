class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_islands = 0

        def dfs(r, c):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            count = 1
            for cx, cy in directions:
                nx, ny = r + cx, c + cy
                if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    count += dfs(nx, ny)
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_islands = max(max_islands, dfs(r, c))

        return max_islands

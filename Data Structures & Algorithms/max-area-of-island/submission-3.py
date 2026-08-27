class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        curr_path = set()

        def dfs(r, c):

            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in curr_path or
                grid[r][c] == 0
            ):
                return 0

            curr_path.add((r, c))
            area = (dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))
            curr_path.remove((r, c))
            grid[r][c] = 0
            return 1 + area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        return res

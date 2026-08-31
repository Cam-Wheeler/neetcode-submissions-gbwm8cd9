class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = [[False for _ in range(COLS)] for _ in range(ROWS)]
        p_visited = set()

        atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)]
        a_visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, grid, visited):
            
            visited.add((r, c))
            grid[r][c] = True
            
            for row_change, col_change in directions:
                r_c, c_c = r + row_change, c + col_change
                if (
                r_c < 0 or
                c_c < 0 or
                r_c >= ROWS or
                c_c >= COLS or
                (r_c, c_c) in visited or
                heights[r_c][c_c] < heights[r][c]
                ):
                    continue
                dfs(r_c, c_c, grid, visited)
            
            return

        # Check pacific
        for r in range(ROWS):
            dfs(r, 0, pacific, p_visited)
        for c in range(COLS):
            dfs(0, c, pacific, p_visited)

        # Check atlantic
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, a_visited)
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, a_visited)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res
            

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0]) # standard rows, cols
        pac, atl = set(), set() # the sets that track where we have been
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # directions

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            for dx, dy in directions:
                dfs(r + dx, c + dy, visited, heights[r][c])
            
            return

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res




class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or
                heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            for dx, dy in directions:
                dfs(r + dx, c + dy, visited, heights[r][c])
            
            return

        
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col]) # Check the row for the pacific
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col]) # Check the row for the atlantic
        
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0]) # check the column for the pacific
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1]) # check the column for the atlantic
        

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res




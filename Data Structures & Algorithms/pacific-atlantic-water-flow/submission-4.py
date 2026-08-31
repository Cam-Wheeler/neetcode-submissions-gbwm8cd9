class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visited, prev_height):

            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in visited or
                heights[r][c] < prev_height
                ):
                    return
            
            visited.add((r, c))
            
            for row_change, col_change in directions:
                r_c, c_c = r + row_change, c + col_change
                dfs(r_c, c_c, visited, heights[r][c])
            
            return

        # Check pacific
        for r in range(ROWS):
            dfs(r, 0, p_visited, heights[r][0])
        for c in range(COLS):
            dfs(0, c, p_visited, heights[0][c])

        # Check atlantic
        for r in range(ROWS):
            dfs(r, COLS - 1, a_visited, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(ROWS - 1, c, a_visited, heights[ROWS - 1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in p_visited and (r, c) in a_visited:
                    res.append([r, c])
        return res
            

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        res = 0

        def dfs(r, c):
            
            # Base case
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in path or
                grid[r][c] == "0"
            ):
                return

            path.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            path.remove((r, c))

            # setting the nodes as we collapse the DFS.
            grid[r][c] = "0"

            return


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    res += 1
                    dfs(row, col)
        
        return res


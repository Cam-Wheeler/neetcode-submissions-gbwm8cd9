class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])


        def dfs(row, col):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for change_x, change_y in directions:
                rd, cd = row + change_x, col + change_y
                if (
                    rd >= 0
                    and cd >= 0
                    and rd < ROWS
                    and cd < COLS
                    and grid[rd][cd] == "1"
                ):
                    grid[rd][cd] = "0"
                    dfs(rd, cd)
            
            return


        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        
        return islands
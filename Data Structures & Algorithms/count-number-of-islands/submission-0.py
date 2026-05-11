class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right

            for change_x, change_y in directions:
                rd, cd = r + change_x, c + change_y
                if (
                    rd >= 0 
                    and cd >= 0
                    and rd < rows
                    and cd < cols
                    and grid[rd][cd] == "1"
                    ):
                    grid[rd][cd] = "0"
                    dfs(rd, cd)

            return


        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands

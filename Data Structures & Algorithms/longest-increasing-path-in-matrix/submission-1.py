class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        memo = {}

        def dfs(i, j):



            if (i, j) in memo:
                return memo[(i, j)]

            res = 1 # this cell.
            for x_change, y_change in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i_c = i + x_change
                j_c = j + y_change
                if (
                    i_c < 0 or
                    i_c == ROWS or
                    j_c < 0 or
                    j_c == COLS or
                    matrix[i][j] <= matrix[i_c][j_c]
                ):
                    continue
                explore = 1 + dfs(i_c, j_c) # future cells.
                res = max(res, explore)
            
            memo[(i, j)] = res

            return memo[(i, j)]
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j))
        return res

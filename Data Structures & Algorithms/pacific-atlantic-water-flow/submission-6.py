from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, prev, visited):
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r, c) in visited
                or heights[r][c] < prev
            ):
                return

            visited.add((r, c))
            h = heights[r][c]
            dfs(r + 1, c, h, visited)
            dfs(r - 1, c, h, visited)
            dfs(r, c + 1, h, visited)
            dfs(r, c - 1, h, visited)

        for col in range(COLS):
            dfs(0, col, heights[0][col], pacific)
            dfs(ROWS - 1, col, heights[ROWS - 1][col], atlantic)

        for row in range(ROWS):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, COLS - 1, heights[row][COLS - 1], atlantic)

        return [[r, c] for r, c in pacific & atlantic]
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        def bfs(r, c):
            queue = deque()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                for change_x, change_y in directions:
                    rd, cd = r + change_x, c + change_y
                    if (rd >= 0
                        and cd >= 0
                        and rd < rows
                        and cd < cols
                        and (rd, cd) not in visited
                        and grid[rd][cd] == "1"):
                        queue.append((rd, cd))




        islands = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)
        
        return islands
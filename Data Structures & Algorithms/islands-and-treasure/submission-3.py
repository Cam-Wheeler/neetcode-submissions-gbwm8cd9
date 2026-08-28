from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        # Seed the queue with the treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        distance = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                for cr, cc in directions:
                    change_r, change_c = r + cr, c + cc
                    if (change_r < 0 or change_c < 0 or 
                        change_r >= ROWS or change_c >= COLS or
                        (change_r, change_c) in visited or
                        grid[change_r][change_c] != INF):
                        continue
                    visited.add((change_r, change_c))
                    q.append((change_r, change_c))
            distance += 1




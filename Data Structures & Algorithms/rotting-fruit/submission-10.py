from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        q = deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for r_change, c_change in directions:
                    rc = r + r_change
                    cc = c + c_change
                    if (
                        rc < 0 or
                        cc < 0 or
                        rc >= ROWS or
                        cc >= COLS or
                        (rc, cc) in visited or
                        grid[rc][cc] != 1
                    ):
                        continue
                    visited.add((rc, cc))
                    q.append((rc, cc))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1 
        

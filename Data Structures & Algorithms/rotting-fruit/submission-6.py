from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        bananas = set()
        q = deque()

        def enqueue(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] != 1):
                return
            visited.add((r, c))
            q.append((r, c))
            return
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    bananas.add((row, col))
                if grid[row][col] == 2:
                    bananas.add((row, col))
                    q.append((row, col))
        
        if not bananas: # Empty grid...
            return 0 

        time = -1 # Cause we need to knock off the rotten ones first! 
        while q:
            for i in range(len(q)):

                r, c = q.popleft()
                bananas.remove((r, c))
                enqueue(r + 1, c)
                enqueue(r - 1, c)
                enqueue(r, c + 1)
                enqueue(r, c - 1)
            time += 1
    
        return -1 if bananas else time





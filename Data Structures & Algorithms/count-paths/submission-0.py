class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DEST = (m - 1, n - 1)
        memo = {}

        def recurse(r: int, c: int, explored: set[tuple[int, int]]):

            if (r, c) == DEST:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]    
            directions = [(0, 1), (1, 0)]
            result = 0
            for direction in directions:
                cx, cy = r + direction[0], c + direction[1]
                if (
                    cx >= 0 and
                    cy >= 0 and
                    cx < m and
                    cy < n and
                    (cx, cy) not in explored
                ):
                    explored.add((cx, cy))
                    result += recurse(cx, cy, explored)
                    explored.remove((cx, cy))
                
                memo[(r, c)] = result

            return memo[(r, c)]
        
        seen = {(0, 0)}
        result = recurse(0, 0, seen)
        return result
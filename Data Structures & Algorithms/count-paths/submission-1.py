class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DEST = (m - 1, n - 1)
        memo = {}

        def recurse(r: int, c: int):

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
                    cy < n
                ):
                    result += recurse(cx, cy)
                
                memo[(r, c)] = result

            return memo[(r, c)]
        
        result = recurse(0, 0)
        return result
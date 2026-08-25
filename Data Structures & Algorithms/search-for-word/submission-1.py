class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        current_path = set()
        
        def dfs(r, c, i):

            if i == len(word):
                return True

            if (r < 0 
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in current_path
                or board[r][c] != word[i]
            ):
                return False

            current_path.add((r, c))
            if (dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1) 
                or dfs(r, c - 1, i + 1)):
                return True
            current_path.remove((r, c))
            return False

        for idx in range(ROWS):
            for jdx in range(COLS):
                if dfs(idx, jdx, 0):
                    return True
        
        return False
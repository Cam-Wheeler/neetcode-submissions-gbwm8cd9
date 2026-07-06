class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r: int, c: int) -> None:
            if board[r][c] != "O":
                return
            board[r][c] = "S"  # mark as safe (connected to border)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc)

        # Step 1: mark all O's connected to the border as safe
        for r in range(ROWS):
            for c in range(COLS):
                if r in (0, ROWS - 1) or c in (0, COLS - 1):
                    dfs(r, c)

        # Step 2: flip everything else
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
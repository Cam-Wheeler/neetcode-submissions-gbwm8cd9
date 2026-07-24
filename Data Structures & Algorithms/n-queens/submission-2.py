class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        pos_diag = set()
        neg_diag = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(row):

            if row == n:
                valid_board = ["".join(row) for row in board]
                res.append(valid_board)
                return


            for c_idx in range(n):
                if c_idx in col or (row + c_idx) in pos_diag or (row - c_idx) in neg_diag:
                    continue
                col.add(c_idx)
                pos_diag.add(row + c_idx)
                neg_diag.add(row - c_idx)
                board[row][c_idx] = "Q"
                dfs(row + 1)
                col.remove(c_idx)
                pos_diag.remove(row + c_idx)
                neg_diag.remove(row - c_idx)
                board[row][c_idx] = "."

            return

        dfs(0)
        return res

                

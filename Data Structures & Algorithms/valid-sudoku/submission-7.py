class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        box_set = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (r, board[r][c]) in row_set:
                    return False
                row_set.add((r, board[r][c]))
                
                if (c, board[r][c]) in col_set:
                    return False
                col_set.add((c, board[r][c]))
                
                if (r // 3, c // 3, board[r][c]) in box_set:
                    return False
                box_set.add((r // 3, c // 3, board[r][c]))

        return True
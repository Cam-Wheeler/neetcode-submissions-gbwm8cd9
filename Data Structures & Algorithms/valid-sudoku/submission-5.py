from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
    
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    continue
                if board[row_idx][col_idx] in rows[row_idx]:
                    return False
                rows[row_idx].add(board[row_idx][col_idx])
                if board[row_idx][col_idx] in cols[col_idx]:
                    return False
                cols[col_idx].add(board[row_idx][col_idx])
                box_key = (row_idx // 3, col_idx // 3)
                if board[row_idx][col_idx] in box[box_key]:
                    return False
                box[box_key].add(board[row_idx][col_idx])
        return True

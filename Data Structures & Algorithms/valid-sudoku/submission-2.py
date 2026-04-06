class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row_idx in range(len(board)):
            row_res = self.check_row(board, row_idx)
            if row_res == False:
                return False
        
        for col_idx in range(len(board)):
            col_res = self.check_col(board, col_idx)
            if col_res == False:
                return False
        
        for row_start_idx in range(0, len(board), 3):
            for col_start_idx in range(0, len(board), 3):
                square_res = self.check_square(board, row_start_idx, col_start_idx)
                if square_res == False:
                    return False
        
        return True

    def check_row(self, board, row_idx) -> bool:
        row_set = set()
        for val in board[row_idx]:
            if val == ".":
                continue
            if val in row_set:
                return False
            else:
                row_set.add(val)
        return True

    def check_col(self, board, col_idx) -> bool:
        col_set = set()
        for row_idx in range(len(board)):
            val = board[row_idx][col_idx]
            if val == ".":
                continue
            if val in col_set:
                return False
            else:
                col_set.add(val)
        return True


    def check_square(self, board, square_row, square_col) -> bool:
        square_set = set()
        square = [row[square_col:square_col+3] for row in board[square_row:square_row+3]]
        for row in square:
            for val in row:
                if val == ".":
                    continue
                if val in square_set:
                    return False
                else:
                    square_set.add(val)
        return True



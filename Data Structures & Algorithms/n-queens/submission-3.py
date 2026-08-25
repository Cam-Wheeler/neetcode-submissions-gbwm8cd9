class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS, COLS = n, n

        col_set = set()
        pos_diag = set()
        neg_diag = set()

        res = []

        def dfs(row, current):

            if row == ROWS:
                res.append(current.copy())
                return

            for col in range(COLS):
                if (
                    col not in col_set and 
                    row + col not in pos_diag and 
                    row - col not in neg_diag
                ):
                    # This is a possible position
                    col_set.add(col)
                    pos_diag.add(row + col)
                    neg_diag.add(row - col)
                    current.append((row, col))

                    # Search more queens
                    dfs(row + 1, current)

                    # Backtrack
                    col_set.remove(col)
                    pos_diag.remove(row + col)
                    neg_diag.remove(row - col)
                    current.pop()
            
            return


        dfs(0, [])

        output = []
        for q_coords in res:
            result = []
            for row in range(ROWS):
                sub_list = []
                for col in range(COLS):
                    if (row, col) in q_coords:
                        sub_list.append("Q")
                    else:
                        sub_list.append(".")
                result.append("".join(sub_list))
            output.append(result)

        return output
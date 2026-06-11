class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        r_set, c_set = set(), set()

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    r_set.add(row)
                    c_set.add(col)

        for row in r_set:
            for idx in range(COLS):
                matrix[row][idx] = 0

        for col in c_set:
            for idx in range(ROWS):
                matrix[idx][col] = 0

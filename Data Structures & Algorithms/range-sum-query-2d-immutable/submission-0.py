class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = 0
        row_min, row_max = row1, row2 + 1
        col_min, col_max = col1, col2 + 1
        for r in range(row_min, row_max):
            for c in range(col_min, col_max):
                region_sum += self.matrix[r][c]
        return region_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        row = self.bsMatrix(matrix, target)
        if row == -1:
            return False
        
        return self.bsRow(matrix[row], target)

    
    def bsMatrix(self, matrix, target) -> int:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                return m
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        return -1

    def bsRow(self, row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif target < row[m]:
                r = m - 1
            else:
                l = m + 1
        return False
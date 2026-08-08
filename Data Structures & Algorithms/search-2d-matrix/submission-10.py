class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row_idx = self.find_row(matrix, l, r, target)
        print(row_idx)
        if row_idx is None:
            return False
        
        row = matrix[row_idx]
        l, r = 0, len(row) - 1
        col_idx = self.find_target(row, l, r, target)
        if col_idx is None:
            return False
        
        return True

    def find_row(self, matrix, left, right, target):
        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                return middle
            elif matrix[middle][0] > target:
                right = middle - 1
            else:
                left = middle + 1
        return None

    def find_target(self, row, left, right, target):
        while left <= right:
            middle = (left + right) // 2
            if row[middle] == target:
                return middle
            elif row[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return None
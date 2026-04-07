class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        result = self.binary_search_matrix(matrix, target)
        if result == -1:
            return False
        return self.binary_search_row(matrix[result], target)


    def binary_search_matrix(self, matrix, target) -> int:
        h = 0
        t = len(matrix) - 1
        while h <= t:
            middle_row = (h + t) // 2
            if matrix[middle_row][0] <= target and matrix[middle_row][-1] >= target:
                return middle_row
            elif matrix[middle_row][0] > target:
                t = middle_row - 1
            else:
                h = middle_row + 1
        return -1

    
    def binary_search_row(self, row, target) -> bool:

        h = 0
        t = len(row) - 1
        while h <= t:
            middle = (h + t) // 2
            if row[middle] == target:
                return True
            elif row[middle] > target:
                t = middle - 1
            else:
                h = middle + 1
        return False
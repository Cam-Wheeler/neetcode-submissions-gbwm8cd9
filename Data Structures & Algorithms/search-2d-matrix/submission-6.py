class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) - 1
        COLS = len(matrix[0]) - 1

        def bs_matrix(l, r):
            
            while l <= r:
                middle = (l + r) // 2
                if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                    return middle
                if matrix[middle][0] > target:
                    r = middle - 1
                else:
                    l = middle + 1
            
            return -1

        def bs_row(row, l, r):
            
            while l <= r:
                middle = (l + r) // 2
                print(middle)
                if matrix[row][middle] == target:
                    return True
                elif matrix[row][middle] < target:
                    l = middle + 1
                else:
                    r = middle - 1
        
            return False
        

        row = bs_matrix(0, ROWS)
        if row == -1:
            return False
        return bs_row(row, 0, COLS)



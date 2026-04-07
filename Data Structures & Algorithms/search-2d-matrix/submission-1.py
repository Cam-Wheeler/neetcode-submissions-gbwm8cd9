class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return self.binary_search(row, target)
        return False
    
    def binary_search(self, row, target) -> bool:

        h = 0
        t = len(row) - 1
        while h <= t:
            middle = (h + t) // 2
            print(row[middle])
            if row[middle] == target:
                return True
            elif row[middle] > target:
                t = middle - 1
            else:
                h = middle + 1
        return False
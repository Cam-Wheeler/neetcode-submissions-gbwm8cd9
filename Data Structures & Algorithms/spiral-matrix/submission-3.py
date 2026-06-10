class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # Top row
            for idx in range(left, right):
                res.append(matrix[top][idx])
            top += 1

            # Right column
            for idx in range(top, bottom):
                res.append(matrix[idx][right - 1]) # Because right is 1 + 
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # Bottom row
            for idx in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][idx])
            bottom -= 1

            # Left column
            for idx in range(bottom - 1, top - 1, -1):
                res.append(matrix[idx][left])
            left += 1

        return res

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Transpose: (0, 1) -> (1, 0), (0, 2) -> (2, 0)
        for i in range(len(matrix)): # Rows
            for j in range(i + 1, len(matrix)): # cols
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

        # We now have the transposed matix, lets flip
        for idx in range(len(matrix)):
            matrix[idx] = matrix[idx][::-1]
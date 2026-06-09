class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ringStart, ringEnd = 0, len(matrix) - 1

        while ringStart < ringEnd:
            for offset in range(ringEnd - ringStart):
                top, bottom = ringStart, ringEnd
                topLeft = matrix[top][ringStart + offset]
                matrix[top][ringStart + offset] = matrix[bottom - offset][ringStart]
                matrix[bottom - offset][ringStart] = matrix[bottom][ringEnd - offset]
                matrix[bottom][ringEnd - offset] = matrix[top + offset][ringEnd]
                matrix[top + offset][ringEnd] = topLeft
            ringStart += 1
            ringEnd -= 1

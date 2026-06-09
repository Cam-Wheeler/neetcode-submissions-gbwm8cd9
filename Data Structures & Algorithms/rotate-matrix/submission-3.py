class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ringStart, ringEnd = 0, len(matrix) - 1

        while ringStart < ringEnd:
            for offset in range(ringEnd - ringStart):
                topLeft = matrix[ringStart][ringStart + offset]

                matrix[ringStart][ringStart + offset] = matrix[ringEnd - offset][ringStart]
                matrix[ringEnd - offset][ringStart]   = matrix[ringEnd][ringEnd - offset]
                matrix[ringEnd][ringEnd - offset]     = matrix[ringStart + offset][ringEnd]
                matrix[ringStart + offset][ringEnd]   = topLeft
            ringStart += 1
            ringEnd -= 1


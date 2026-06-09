class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ringStart, ringEnd = 0, len(matrix) - 1

        while ringStart < ringEnd:
            for offset in range(ringEnd - ringStart):
                top, bottom = ringStart, ringEnd

                # save the top-left
                topLeft = matrix[top][ringStart + offset]

                # move bottom-left into top-left
                matrix[top][ringStart + offset] = matrix[bottom - offset][ringStart]

                # move bottom-right into bottom-left
                matrix[bottom - offset][ringStart] = matrix[bottom][ringEnd - offset]

                # move top-right into bottom-right
                matrix[bottom][ringEnd - offset] = matrix[top + offset][ringEnd]

                # move top-left (saved) into top-right
                matrix[top + offset][ringEnd] = topLeft

            ringEnd -= 1
            ringStart += 1
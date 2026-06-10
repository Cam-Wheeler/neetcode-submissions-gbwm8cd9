class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        h_start, h_end = 0, len(matrix) - 1
        w_start, w_end = 0, len(matrix[0]) - 1

        while (h_start <= h_end) and (w_start <= w_end):

            # Top row
            for offset in range(w_start, w_end + 1):
                res.append(matrix[h_start][offset])

            if h_start == h_end:
                break

            # Right column
            for offset in range(h_start + 1, h_end + 1):
                res.append(matrix[offset][w_end])

            if w_start == w_end:
                break
            
            # Bottom row
            for offset in range(w_end - 1, w_start - 1, - 1):
                res.append(matrix[h_end][offset])
            
            # Left column
            for offset in range(h_end - 1, h_start, - 1):
                res.append(matrix[offset][w_start])

            h_start += 1
            h_end -= 1
            w_start += 1
            w_end -= 1
        
        print(res)
        return res


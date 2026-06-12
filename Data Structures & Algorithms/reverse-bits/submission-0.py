class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        for i in range(32):
            bit = n & 1
            n = n >> 1
            res = res << 1
            if bit == 1:
                res = res | 1
            else:
                res = res | 0
        return res

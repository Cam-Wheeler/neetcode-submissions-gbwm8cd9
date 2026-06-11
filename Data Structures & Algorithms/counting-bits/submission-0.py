class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0, n + 1):
            current = 0
            for i in range(32):
                if num & (1 << i):
                    current += 1
            res.append(current)
        return res
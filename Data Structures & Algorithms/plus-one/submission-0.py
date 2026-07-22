class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        over_flow = 0
        idx = len(digits) - 1
        while idx > -1:
            val = digits[idx]
            if idx == len(digits) - 1 or over_flow:
                val = val + 1
                if val >= 10:
                    val = 0
                    over_flow = 1
                else:
                    over_flow = 0
            res.append(val)
            idx -= 1

        if over_flow:
            res.append(1)
        
        return res[::-1]

            
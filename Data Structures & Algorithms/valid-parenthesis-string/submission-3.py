class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1   # treat as ')'
                hi += 1   # treat as '('
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:

            if n in seen:
                return False
            
            new_val = 0
            s_n = str(n)
            for char in s_n:
                new_val += int(char)**2
            
            seen.add(n)
            n = new_val
        
        return True
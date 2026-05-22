class Solution:
    def countSubstrings(self, s: str) -> int:
        
        result = 0
        n = len(s)

        for idx in range(len(s)):
            result += self.check_palindrome(idx, idx, s)
            result += self.check_palindrome(idx, idx + 1, s)
        
        return result

    
    def check_palindrome(self, l, r, s) -> int:

        res = 0

        while (l >= 0 and r < len(s) and s[l] == s[r]):
            res += 1
            l -= 1
            r += 1
        return res


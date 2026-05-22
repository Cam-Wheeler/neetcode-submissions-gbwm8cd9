class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def check_palindrome(l, r):
            nonlocal result 

            while (l >= 0 and r < len(s) and s[l] == s[r]):
                result += 1
                l -= 1
                r += 1
            
            return

        for idx in range(len(s)):
            check_palindrome(idx, idx)
            check_palindrome(idx, idx + 1)

        return result

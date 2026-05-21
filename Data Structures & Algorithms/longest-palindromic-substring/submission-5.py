class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        def grow_palindrome(l, r):
            nonlocal res

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1
            return

        for idx in range(len(s)):

            grow_palindrome(idx, idx)
            grow_palindrome(idx, idx+1)

        return res



    
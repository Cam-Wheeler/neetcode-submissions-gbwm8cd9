class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def check_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = s[0]  # single char is always a palindrome, handles empty result case

        for idx in range(n):
            # Prune: even if everything left is a palindrome, can't beat current best
            if (n - idx) < len(res):
                break

            for jdx in range(n - 1, idx, -1):  # iterate from end, longest first
                # Skip substrings that can't beat current best
                if jdx - idx + 1 <= len(res):
                    break

                if s[jdx] == s[idx] and check_palindrome(idx, jdx):
                    res = s[idx:jdx + 1]
                    break  # longest for this idx found, move on

        return res
        



    
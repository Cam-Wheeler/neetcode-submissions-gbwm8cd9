class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(l, r, del_flag):

            while l <= r:
                if s[l] != s[r]:
                    if del_flag:
                        return False
                    res = is_palindrome(l + 1, r, True) or is_palindrome(l, r - 1, True)
                    return res
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        return is_palindrome(l, r, False)
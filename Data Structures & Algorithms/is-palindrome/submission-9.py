class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalpha():
                cleaned = cleaned + char.lower()
            if char.isnumeric():
                cleaned = cleaned + char

        l, r = 0, len(cleaned) - 1
        while l <= r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True
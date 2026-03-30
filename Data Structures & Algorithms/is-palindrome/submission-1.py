class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char
        cleaned = cleaned.lower()
        
        head = 0
        tail = len(cleaned) - 1
        while head < tail:
            print(cleaned[head], cleaned[tail])
            if cleaned[head] != cleaned[tail]:
                return False
            head += 1
            tail -= 1
        return True
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        for char in s:
            counts_s[char] = 1 + counts_s.get(char, 0)
        
        counts_t = {}
        for char in t:
            counts_t[char] = 1 + counts_t.get(char, 0)

        return counts_s == counts_t        

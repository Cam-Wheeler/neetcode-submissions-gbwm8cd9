from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        if s == t:
            return True
        return False
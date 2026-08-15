class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev = s[0]
        for idx in range(1, len(s)):
            score += abs(ord(prev) - ord(s[idx]))
            prev = s[idx]
        return score
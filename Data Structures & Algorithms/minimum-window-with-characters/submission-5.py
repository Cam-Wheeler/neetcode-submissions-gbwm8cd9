from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        counts = Counter(t)
        required_matches = len(counts)
        min_window = float("inf")
        res = ""
        for l in range(len(s)):
            if s[l] in counts:
                compare = defaultdict(int)
                for r in range(l, len(s)):
                    if s[r] in counts:
                        compare[s[r]] += 1
                    matches = 0        
                    for char in counts:
                        if compare[char] < counts[char]:
                            break
                        matches += 1
                    if matches == required_matches and r + 1 - l < min_window:
                        min_window = r + 1 - l
                        res = s[l:r+1]

        return res

        
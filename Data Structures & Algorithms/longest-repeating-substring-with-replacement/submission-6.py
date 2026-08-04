from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        counts = defaultdict(int)
        l, r = 0, 0
        max_seq = 0

        while r < len(s):
            char = s[r]
            counts[char] += 1
            max_char = max(counts.values())
            replacements = sum(counts.values()) - max_char
            while replacements > k:
                counts[s[l]] -= 1
                replacements -= 1
                l += 1
            max_seq = max(max_seq, r - l + 1)
            r += 1
        
        return max_seq

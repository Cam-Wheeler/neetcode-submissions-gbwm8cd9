from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        tracker = defaultdict(int)
        max_char = 0
        head, tail = 0, 0

        while tail < len(s):
            tracker[s[tail]] += 1
            max_char = max(tracker.values())
            replacements = sum(tracker.values()) - max_char
            while replacements > k:
                tracker[s[head]] -= 1
                head += 1
                max_char = max(tracker.values())
                replacements = sum(tracker.values()) - max_char
            res = max(res, tail - head)
            tail += 1
        return res + 1


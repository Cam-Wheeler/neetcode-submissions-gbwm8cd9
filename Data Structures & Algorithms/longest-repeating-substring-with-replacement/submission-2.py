from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        tracker = defaultdict(int)
        head, tail = 0, 0

        while tail < len(s):
            tracker[s[tail]] += 1
            replacements = sum(tracker.values()) - max(tracker.values())
            while replacements > k:
                tracker[s[head]] -= 1
                head += 1
                replacements = sum(tracker.values()) - max(tracker.values())
            res = max(res, tail - head)
            tail += 1
        return res + 1


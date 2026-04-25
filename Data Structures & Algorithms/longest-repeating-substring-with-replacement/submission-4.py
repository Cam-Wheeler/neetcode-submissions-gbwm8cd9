from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        tracker = defaultdict(int)
        head = 0

        for tail in range(len(s)):
            tracker[s[tail]] += 1
            replacements = (tail - head) + 1 - max(tracker.values())
            while replacements > k:
                tracker[s[head]] -= 1
                head += 1
                replacements = (tail - head) + 1  - max(tracker.values())
            res = max(res, tail - head)
        return res + 1


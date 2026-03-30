from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if (len(s)) == 1:
            return 1

        counts = defaultdict(int)
        head = tail = 0
        max_seq_len = 0

        while tail < len(s):
            counts[s[tail]] += 1
            print(counts)
            common_char_count = max(counts.values())
            replacements = sum(counts.values()) - common_char_count
            while replacements > k:
                dropped_char = s[head]
                head += 1
                counts[dropped_char] -= 1
                replacements = sum(counts.values()) - max(counts.values())
            max_seq_len = max(max_seq_len, (tail - head) + 1)
            tail += 1
        
        return max_seq_len
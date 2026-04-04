class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        head, tail = 0, 0
        max_seq_len = 0

        while tail < len(s):
            if s[tail] in char_set:
                while s[tail] in char_set:
                    char_set.remove(s[head])
                    head += 1
            char_set.add(s[tail])
            diff = (tail - head) + 1
            max_seq_len = max(max_seq_len, diff)
            tail += 1
        return max_seq_len
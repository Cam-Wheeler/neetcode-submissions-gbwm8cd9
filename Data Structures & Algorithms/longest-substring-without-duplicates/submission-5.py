class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        head, tail = 0, 0
        max_diff = 0
        while tail < len(s):
            if s[tail] in char_set:
                max_diff = max(max_diff, (tail - head))
                while s[tail] in char_set:
                    char_set.remove(s[head])
                    head += 1
            char_set.add(s[tail])
            tail += 1
        return max(max_diff, tail - head)
            
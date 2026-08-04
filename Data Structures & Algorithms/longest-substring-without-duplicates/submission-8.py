class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        seq_chars = set()
        head = 0
        tail = 0
        res = 0
        while head < len(s):
            # Check its not already in there.
            while s[head] in seq_chars:
                seq_chars.remove(s[tail])
                tail += 1
            
            seq_chars.add(s[head])
            res = max(res, len(seq_chars))
            head += 1
        return res
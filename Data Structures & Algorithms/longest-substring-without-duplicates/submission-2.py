class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        counter = set()
        head = 0
        tail = 1
        current_max_seq = 0
        counter.add(s[head])

        while tail < len(s):
            char = s[tail]
            if char in counter:
                current_max_seq = max(current_max_seq, tail - head)
                while s[head] != char:
                    counter.remove(s[head])
                    head += 1
                counter.remove(s[head])
                head += 1
            counter.add(s[tail])
            tail += 1
        current_max_seq = max(current_max_seq, tail - head)
        return current_max_seq



            
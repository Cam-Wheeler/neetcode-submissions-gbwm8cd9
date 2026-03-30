from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return "" # Impossible to contain all of t, s is shorter! 

        t_dict = Counter(t)
        
        head = tail = 0
        shortest_seq_seen_len = None
        shortest_seq_seen = None

        while tail < len(s):
            seq_dict = Counter(s[head:tail+1])
            while t_dict <= seq_dict:
                if shortest_seq_seen_len == None or len(seq_dict) < shortest_seq_seen_len:
                    shortest_seq_seen_len = (tail + 1) - head
                    shortest_seq_seen = s[head:tail+1]
                head += 1
                seq_dict = Counter(s[head:tail+1])
            tail+= 1
        return shortest_seq_seen if shortest_seq_seen else ""
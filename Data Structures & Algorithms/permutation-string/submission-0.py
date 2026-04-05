from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_str_len = len(s1)
        sub_str = defaultdict(int)
        current_str = defaultdict(int)

        for s in s1:
            sub_str[s] += 1

        head, tail = 0, 0

        while tail < len(s2):
            if (tail - head) < sub_str_len:
                current_str[s2[tail]] += 1
                tail += 1

            if (tail - head) == sub_str_len:
                if sub_str == current_str:
                    return True
                else:
                    current_str[s2[head]] -= 1
                    if current_str[s2[head]] == 0:
                        del current_str[s2[head]]
                    head += 1

        return False
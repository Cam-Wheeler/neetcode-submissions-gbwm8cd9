class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_idx = {}
        for idx, char in enumerate(s):
            last_idx[char] = idx

        size, end = 0, 0
        for idx in range(len(s)):
            size += 1
            end = max(end, last_idx[s[idx]])

            if idx == end:
                res.append(size)
                size = 0
        
        return res
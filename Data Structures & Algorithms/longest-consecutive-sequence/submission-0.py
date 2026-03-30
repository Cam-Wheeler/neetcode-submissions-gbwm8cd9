class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)

        max_seq_len = 0
        for val in vals:
            if val - 1 not in vals: # We have a sequence start.
                seq_len = 1
                start = val
                while start + 1 in vals:
                    seq_len += 1
                    start += 1
                if seq_len > max_seq_len:
                    max_seq_len = seq_len
        return max_seq_len



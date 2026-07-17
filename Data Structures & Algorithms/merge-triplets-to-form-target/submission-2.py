class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for idx in range(len(t)):
                if t[idx] == target[idx]:
                    valid.add(idx)

        if len(valid) == 3:
            return True
        return False
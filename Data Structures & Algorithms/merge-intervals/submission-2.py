class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        res = []
        current = intervals[0]

        for start, end in intervals[1:]:
            if start <= current[1]:
                current[1] = max(current[1], end)
            else:
                res.append(current)
                current = [start, end]
        
        res.append(current)
        return res
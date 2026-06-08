class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        start = newInterval[0]
        end = newInterval[1]
        idx = 0

        while idx < len(intervals) and intervals[idx][1] < start:
            res.append(intervals[idx])
            idx += 1

        # We are now at the point where the intervals need to be merged (if required)
        while (
            idx < len(intervals)
            and intervals[idx][0] <= end
        ):
            start = min(intervals[idx][0], start)
            end = max(intervals[idx][1], end)
            idx += 1

        # We have merged if needed lets add our new Interval.
        res.append([start, end])

        # Add the remaining following it.
        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1

        return res

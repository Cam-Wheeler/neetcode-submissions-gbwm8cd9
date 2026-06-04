"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)

        stack = deque()
        for interval in intervals:            
            if stack and interval.start < stack[-1]:
                return False
            
            stack.append(interval.end)
        
        return True
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        stored = self.cache[key]
        if len(stored) == 0:
            return ""

        l, r = 0, len(stored) - 1
        while l <= r:
            m = (l + r) // 2
            value, prev_time = stored[m]

            if prev_time == timestamp:
                return value
            
            if prev_time > timestamp:
                r = m - 1
            
            if prev_time < timestamp:
                l = m + 1
        return stored[r][0] if stored[r][1] <= timestamp else ""
            
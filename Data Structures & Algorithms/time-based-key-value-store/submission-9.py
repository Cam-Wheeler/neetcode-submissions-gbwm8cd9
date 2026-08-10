from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        stored = self.cache[key]
        res = ""

        l, r = 0, len(stored) - 1
        while l <= r:
            m = (l + r) // 2
            value, prev_time = stored[m]
            if prev_time > timestamp:
                r = m - 1
            elif prev_time <= timestamp:
                res = value
                l = m + 1

        return res
            
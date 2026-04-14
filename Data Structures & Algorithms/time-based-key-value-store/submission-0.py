from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        values = self.cache[key]
        for idx in range(len(values) - 1, -1, -1):
            if values[idx][1] <= timestamp:
                return values[idx][0]
        return ""

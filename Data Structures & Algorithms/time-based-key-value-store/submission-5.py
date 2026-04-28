from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        
        for idx in range(len(self.cache[key]) - 1, -1, -1):
            if self.cache[key][idx][0] <= timestamp:
                return self.cache[key][idx][1]
        
        return ""

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        for tpl in self.buckets[self._hash(key)]:
            if tpl[0] == key:
                self.remove(key)
        self.buckets[self._hash(key)].append((key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        for k, val in bucket:
            if k == key:
                return val
        return -1 

    def remove(self, key: int) -> None:
        bucket = [tpl for tpl in self.buckets[self._hash(key)] if tpl[0] != key]
        self.buckets[self._hash(key)] = bucket
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
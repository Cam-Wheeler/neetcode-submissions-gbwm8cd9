class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hashset = [[] for i in range(self.size)]
        

    def add(self, key: int) -> None:
        bucket_idx = key % self.size
        if key not in self.hashset[bucket_idx]:
            self.hashset[bucket_idx].append(key)
        
    def remove(self, key: int) -> None:
        bucket_idx = key % self.size
        if key in self.hashset[bucket_idx]:
            self.hashset[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = key % self.size
        if key in self.hashset[bucket_idx]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
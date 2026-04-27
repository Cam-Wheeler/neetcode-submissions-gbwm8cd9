class DoubleNode(object):
    
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleNode(-1, -1)
        self.tail = DoubleNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        previous_node = self.tail.prev
        previous_node.next = node
        self.tail.prev = node
        node.prev = previous_node
        node.next = self.tail
    
    def remove(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = DoubleNode(key, value)
        self.cache[key] = node
        self.insert(node)
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]


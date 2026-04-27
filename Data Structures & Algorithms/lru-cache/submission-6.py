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
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.insert(node)
        else:
            node = DoubleNode(key, value)
            self.insert(node)
            self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.remove(self.head.next)
            del self.cache[lru.key]


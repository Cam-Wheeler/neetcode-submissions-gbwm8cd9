class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1 

    def put(self, key: int, value: int) -> None:

        node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]

        

        

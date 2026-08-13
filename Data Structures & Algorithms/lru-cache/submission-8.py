class ListNode:

    def __init__(self, value: int = -1, key = -1, nxt = None, prev = None) -> None:
        self.value = value
        self.nxt = nxt
        self.key = key
        self.prev = prev

        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key --> node
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = ListNode(key=key, value=value)
        self._insert(node)

        while len(self.cache) > self.capacity:
            self._remove(self.head.nxt)

    def _insert(self, node) -> None:
        prev_node = self.tail.prev
        self.tail.prev = node
        prev_node.nxt = node
        node.nxt = self.tail
        node.prev = prev_node
        self.cache[node.key] = node

    def _remove(self, node) -> None:
        prev_node = node.prev
        next_node = node.nxt
        prev_node.nxt = next_node
        next_node.prev = prev_node
        node.nxt, node.prev = None, None
        del self.cache[node.key]

        

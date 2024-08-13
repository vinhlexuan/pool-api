class Node:
    def __init__(self, key, value) -> None:
        self.key, self.value = key, value
        self.prev, self.next = None, None
        pass

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        prev, right = node.prev, node.next
        prev.next, right.prev = right, prev

    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        
    def get(self, key: int) -> list[int]:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return []
    
    def put(self, key: int, value: list[int]):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
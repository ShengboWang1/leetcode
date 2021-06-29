class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.protect = ListNode()
        self.tail = ListNode()
        self.protect.next = self.tail
        self.tail.prev = self.protect
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}

    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            value = node.value
            self.removeFromList(key)
            self.addToFront(key, value)
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.hashmap:
            self.removeFromList(key)
            self.addToFront(key, value)
        else:
            if self.size >= self.capacity:
                self.removeFromList(self.tail.prev.key)
                self.addToFront(key, value)
            else:
                self.addToFront(key, value)
                self.size += 1

    def addToFront(self, key, value):
        curr = ListNode(key, value)
        curr.next = self.protect.next
        self.protect.next = curr
        curr.prev = self.protect
        curr.next.prev = curr
        self.hashmap[key] = curr

    def removeFromList(self, key):
        curr = self.hashmap[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.hashmap.pop(key)
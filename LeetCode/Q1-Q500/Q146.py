class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.count = 0

    def get(self, key: int) -> int:
        self.count += 1
        if key in self.cache:
            self.cache[key][1] = self.count
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.count += 1
        if key in self.cache or len(self.cache) < self.capacity:
            self.cache[key] = [value, self.count]
        else:
            LRU = list(self.cache.keys())[0]
            for cKey, cVal in self.cache.items():
                used = cVal[1]
                if used < self.cache[LRU][1]: LRU = cKey
            del self.cache[LRU]
            self.cache[key] = [value, self.count]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
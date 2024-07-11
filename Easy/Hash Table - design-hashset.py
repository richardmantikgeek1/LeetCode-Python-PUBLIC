class MyHashSet:

    def __init__(self):
        self.map = {}

    def add(self, key):
        self.map[key] = True

    def remove(self, key):
        if (self.contains(key)):
            self.map.pop(key)

    def contains(self, key):
        return key in self.map.keys()


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
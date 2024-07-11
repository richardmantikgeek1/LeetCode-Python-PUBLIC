class MyHashMap:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        has_key = False
        for pair in self.map:
            if (pair[0] == key):
                pair[1] = value
                has_key = True
        if (not has_key):
            self.map.append([key, value])

    def get(self, key):
        for pair in self.map:
            if (pair[0] == key):
                return pair[1]
        return -1

    def remove(self, key):
        for i in range(0, len(self.map)):
            pair = self.map[i]
            if (pair[0] == key):
                self.map.pop(i)
                return
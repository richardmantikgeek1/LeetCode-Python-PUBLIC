class OrderedStream:

    def __init__(self, n):
        self.array  = [None] * n
        self.ptr    = 0
        self.size   = n

    def insert(self, idKey, value):
        self.array[idKey-1] = value
        ret_val = []
        if (self.ptr == idKey-1):
            while(self.ptr < self.size and self.array[self.ptr] is not None):
                ret_val.append(self.array[self.ptr])
                self.ptr += 1

        return ret_val

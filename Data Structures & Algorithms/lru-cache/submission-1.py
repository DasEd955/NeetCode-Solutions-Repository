class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = list()

    def get(self, key: int) -> int:
        for index, item in enumerate(self.cache):
            if item[0] == key:
                temp = self.cache.pop(index)
                self.cache.append(temp)
                return temp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for index, item in enumerate(self.cache):
            if item[0] == key:
                temp = self.cache.pop(index)
                temp[1] = value
                self.cache.append(temp)
                return
        if self.capacity == len(self.cache):
            self.cache.pop(0)
        self.cache.append([key, value])

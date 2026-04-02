class TimeMap:

    def __init__(self):
        self.kvtMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvtMap:
            self.kvtMap[key] = list()
        self.kvtMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvtMap:
            return ""
        
        result, values = str(), self.kvtMap.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return result

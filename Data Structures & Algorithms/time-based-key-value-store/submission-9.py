class TimeMap:

    def __init__(self):
        self.kvtMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvtMap:
            self.kvtMap[key] = []
        self.kvtMap[key].append((value, timestamp))
        print(self.kvtMap)

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.kvtMap:
            return ""

        output = str()
        left, right = 0, len(self.kvtMap[key]) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if self.kvtMap[key][middle][1] == timestamp:
                return self.kvtMap[key][middle][0]
            elif self.kvtMap[key][middle][1] < timestamp:
                left = middle + 1
            else:
                right = middle - 1  

        return self.kvtMap[key][right][0] if right != -1 else ""
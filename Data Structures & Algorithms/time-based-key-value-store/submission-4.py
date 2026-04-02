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

        output = ""

        for i in range(len(self.kvtMap[key])):
            if self.kvtMap[key][i][1] <= timestamp:
                output = self.kvtMap[key][i][0]
        
        return output
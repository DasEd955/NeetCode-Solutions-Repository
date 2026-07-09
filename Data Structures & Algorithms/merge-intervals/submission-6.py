class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals

        result = list()
        intervals.sort()
        
        for i in range(len(intervals) - 1):
            if not result:
                result.append(intervals[i])
            if result[-1][1] >= intervals[i + 1][0]:
                result[-1] = [min(result[-1][0], intervals[i + 1][0]), max(result[-1][1], intervals[i + 1][1])]
            else:
                result.append(intervals[i + 1])
        
        return result
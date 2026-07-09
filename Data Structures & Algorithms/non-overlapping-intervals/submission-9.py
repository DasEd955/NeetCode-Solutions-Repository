class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for i in range(len(intervals) - 1):
            if prevEnd > intervals[i + 1][0]:
                prevEnd = min(prevEnd, intervals[i + 1][1])
                result += 1
            else:
                prevEnd = intervals[i + 1][1]

        return result
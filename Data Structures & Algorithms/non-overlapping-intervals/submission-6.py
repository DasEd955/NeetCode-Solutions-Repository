class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        print(intervals)

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                intervals.pop(i + 1 if intervals[i + 1][1] > intervals[i][1] else i)
                result += 1
            else:
                i += 1 
        
        return result
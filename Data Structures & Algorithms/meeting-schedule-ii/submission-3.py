"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = list(), list()
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts, ends = sorted(starts), sorted(ends)

        p1, p2 = 0, 0
        current, maxRooms = 0, 0
        while p1 < len(starts):
            if starts[p1] < ends[p2]:
                p1 += 1
                current += 1
            else:
                p2 += 1
                current -= 1
            maxRooms = max(maxRooms, current)
        
        return maxRooms
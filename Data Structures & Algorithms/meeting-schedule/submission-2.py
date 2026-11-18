#Sorting
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda inter: inter.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if min(i1.end, i2.end)>max(i1.start,i2.start):
                return False
        return True 

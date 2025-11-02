"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = [iv for emp in schedule for iv in emp]

        intervals.sort(key=lambda x: x.start)

        res = []
        prev_end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start > prev_end:
                res.append(Interval(prev_end, intervals[i].start))
            prev_end = max(prev_end, intervals[i].end)
        return res
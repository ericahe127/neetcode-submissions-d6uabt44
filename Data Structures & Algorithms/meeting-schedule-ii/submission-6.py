"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        intervals.sort(key = lambda intervals: intervals.start)
        pq = [intervals[0].end]

        for i in range(1, len(intervals)):
            if intervals[i].start >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, intervals[i].end)

        return len(pq)

        
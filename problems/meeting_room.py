# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms
import unittest


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals or len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        size = len(intervals)
        for i in range(size - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True


class TestMeetingRoom(unittest.TestCase):
    def test(self):
        sol = Solution()
        intervals = [Interval(i, j) for i, j in [[0, 30], [5, 10], [15, 20]]]
        self.assertFalse(sol.canAttendMeetings(intervals))
        intervals = [Interval(i, j) for i, j in [[7, 10], [2, 4]]]
        self.assertTrue(sol.canAttendMeetings(intervals))


if __name__ == '__main__':
    unittest.TestCase()

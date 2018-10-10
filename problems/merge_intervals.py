# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals
import unittest


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        merge = []
        for interval in intervals:
            if not merge or merge[-1].end < interval.start:
                merge.append(interval)
            else:
                merge[-1].end = max(merge[-1].end, interval.end)
        return merge


class TestMergeIntervals(unittest.TestCase):
    def test(self):
        sol = Solution()
        data = [Interval(i, j) for i, j in [[1, 3], [2, 6], [8, 10], [15, 18]]]
        ret = [[node.start, node.end] for node in sol.merge(data)]
        self.assertEqual(ret,
            [[1, 6], [8, 10], [15, 18]]
        )
        data = [Interval(i, j) for i, j in [[1, 4], [4, 5]]]
        ret = [[node.start, node.end] for node in sol.merge(data)]
        self.assertEqual(
            ret,
            [[1, 5]]
        )


if __name__ == '__main__':
    unittest.TestCase()

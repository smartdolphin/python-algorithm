# 636. Exclusive Time of Functions
# https://leetcode.com/problems/exclusive-time-of-functions
import unittest


class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not logs:
            return []

        s = logs[0].split(':')
        prev = int(s[2])
        stack = [int(s[0])]
        res = [0] * n

        for log in logs[1:]:
            s = log.split(':')
            if s[1] == 'start':
                if stack:
                    res[stack[-1]] += int(s[2]) - prev
                stack.append(int(s[0]))
                prev = int(s[2])
            else:
                res[stack.pop()] += int(s[2]) - prev + 1
                prev = int(s[2]) + 1
        return res


class TestExclusiveTime(unittest.TestCase):
    def test(self):
        sol = Solution()
        n = 2
        logs = [
            "0:start:0",
            "1:start:2",
            "1:end:5",
            "0:end:6"
        ]
        self.assertEqual(
            sol.exclusiveTime(n, logs),
            [3, 4]
        )


if __name__ == '__main__':
    unittest.TestCase()

# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin
import unittest


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cnt = {'L': 0,
               'R': 0,
               'U': 0,
               'D': 0}
        for direction in moves:
            cnt[direction] += 1
        return cnt['L'] == cnt['R'] and cnt['U'] == cnt['D']


class TestRobotToOrigin(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(
            sol.judgeCircle('UD')
        )
        self.assertTrue(
            sol.judgeCircle('LR')
        )
        self.assertFalse(
            sol.judgeCircle('RR')
        )
        self.assertFalse(
            sol.judgeCircle('DDR')
        )
        self.assertTrue(
            sol.judgeCircle('DDUU')
        )


if __name__ == '__main__':
    unittest.TestCase()

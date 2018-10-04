# 231. Power of Two
# https://leetcode.com/problems/power-of-two
import unittest


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return self.isPowerOfTwo(n // 2)


class TestIsPowerOfTwo(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(
            sol.isPowerOfTwo(2)
        )
        self.assertTrue(
            sol.isPowerOfTwo(16)
        )
        self.assertFalse(
            sol.isPowerOfTwo(3)
        )
        self.assertFalse(
            sol.isPowerOfTwo(-1)
        )
        self.assertFalse(
            sol.isPowerOfTwo(0)
        )
        self.assertFalse(
            sol.isPowerOfTwo(218)
        )


if __name__ == '__main__':
    unittest.TestCase()

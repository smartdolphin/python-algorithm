# 326. Power of Three
# https://leetcode.com/problems/power-of-three
import unittest


class Solution(object):
    # Time: O(log3N), Space: O(1)
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

    # Time: O(log3N), Space: O(log3N)
    def _isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)


class TestIsPowerOfTwo(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(
            sol.isPowerOfThree(9)
        )
        self.assertTrue(
            sol.isPowerOfThree(3)
        )
        self.assertFalse(
            sol.isPowerOfThree(99)
        )
        self.assertFalse(
            sol.isPowerOfThree(4)
        )
        self.assertFalse(
            sol.isPowerOfThree(0)
        )
        self.assertFalse(
            sol.isPowerOfThree(1)
        )


if __name__ == '__main__':
    unittest.TestCase()

# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n
import unittest


class Solution:
    # Time complexity: O(log(n))
    # Space complexity: O(log(n))
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        return self._fast_pow(x, n)

    def _fast_pow(self, x, n):
        if n == 0:
            return 1

        half = self._fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    # Time complexity: O(n)
    # Space complexity: O(1)
    def myPow_bruteForce(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        ret = 1
        for _ in range(n):
            ret *= x

        return ret


class TestPow(unittest.TestCase):
    def test(self):
        # Your MinStack object will be instantiated and called as such:
        sol = Solution()
        self.assertEqual(
            sol.myPow(2.0, 10),
            1024.0
        )
        self.assertEqual(
            round(sol.myPow(2.1, 3), 4),
            9.261
        )
        self.assertEqual(
            sol.myPow(2, -2),
            0.25
        )


if __name__ == '__main__':
    unittest.TestCase()

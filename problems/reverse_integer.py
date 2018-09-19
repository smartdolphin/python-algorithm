# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer

import unittest


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        result = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        while x > 0:
            tail = x % 10
            result = (result * 10) + tail
            x = x // 10

        if is_negative:
            result = -result

        if result < -(2 ** 31) or (2 ** 31 - 1) < result:
            result = 0
        return result


class ReverseTest(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()
        self.assertEqual(
            solution.reverse(123), 321
        )
        self.assertEqual(
            solution.reverse(-123), -321
        )
        self.assertEqual(
            solution.reverse(120), 21
        )


if __name__ == '__main__':
    unittest.main()

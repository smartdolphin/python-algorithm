# 66. Plus One
# https://leetcode.com/problems/plus-one
import unittest


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        digits.insert(0, 1)
        return digits


class TestPlusOne(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.plusOne([1, 2, 3]),
            [1, 2, 4]
        )
        self.assertEqual(
            sol.plusOne([9, 9]),
            [1, 0, 0]
        )
        self.assertEqual(
            sol.plusOne([9, 8]),
            [9, 9]
        )
        self.assertEqual(
            sol.plusOne([1, 9, 9]),
            [2, 0, 0]
        )
        self.assertEqual(
            sol.plusOne([9]),
            [1, 0]
        )


if __name__ == '__main__':
    unittest.TestCase()

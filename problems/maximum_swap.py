# 670. Maximum Swap
# https://leetcode.com/problems/maximum-swap
import unittest


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = list(str(num))
        size = len(arr)
        if size == 1:
            return num

        for i in range(size):
            for j in range(i + 1, size):
                self.swap(arr, i, j)
                val = int(''.join(arr))
                if val > num:
                    num = val
                self.swap(arr, i, j)
        return num

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


class TestMaximumSwap(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.maximumSwap(2736),
            7236
        )
        self.assertEqual(
            sol.maximumSwap(1),
            1
        )
        self.assertEqual(
            sol.maximumSwap(10),
            10
        )


if __name__ == '__main__':
    unittest.TestCase()

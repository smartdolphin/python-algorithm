# 344. Reverse String
# https://leetcode.com/problems/reverse-string
import unittest


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1:
            return s

        arr = list(s)
        left = 0
        right = size - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return ''.join(arr)


class TestReverseString(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.reverseString('abc'),
            'cba'
        )
        self.assertEqual(
            sol.reverseString('cad'),
            'dac'
        )


if __name__ == '__main__':
    unittest.TestCase()

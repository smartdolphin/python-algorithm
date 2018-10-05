# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer
import unittest


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        size = len(s)
        for i in range(size):
            if i + 1 < size and dic[s[i]] < dic[s[i + 1]]:
                result -= dic[s[i]]
            else:
                result += dic[s[i]]
        return result


class TestRomanToInt(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.romanToInt('III'),
            3
        )
        self.assertEqual(
            sol.romanToInt('IV'),
            4
        )
        self.assertEqual(
            sol.romanToInt('IX'),
            9
        )
        self.assertEqual(
            sol.romanToInt('LVIII'),
            58
        )
        self.assertEqual(
            sol.romanToInt('MCMXCIV'),
            1994
        )


if __name__ == '__main__':
    unittest.TestCase()

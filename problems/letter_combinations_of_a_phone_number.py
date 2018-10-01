# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
import unittest


class Solution:
    def __init__(self):
        self.dic = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['q', 'p', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not isinstance(digits, str):
            raise ValueError('input should be string')

        ret = []
        for n in digits:
            try:
                n = int(n)
            except ValueError:
                return []

            if n in self.dic:
                if not ret:
                    ret = self.dic[n]
                else:
                    temp = []
                    for s in ret:
                        for c in self.dic[n]:
                            temp.append(s + c)
                    ret = temp
        return ret


class TestNumOfIsland(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.letterCombinations('23'),
            ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        )
        self.assertEqual(
            sol.letterCombinations('2'),
            ['a', 'b', 'c']
        )


if __name__ == '__main__':
    unittest.TestCase()

# 760. Find Anagram Mappings
# https://leetcode.com/problems/find-anagram-mappings
import unittest


class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {b: i for i, b in enumerate(B)}
        return [dic[a] for a in A]


class TestLetterCasePermutation(unittest.TestCase):
    def test(self):
        sol = Solution()
        a = [12, 28, 46, 32, 50]
        b = [50, 12, 32, 46, 28]
        self.assertEqual(
            sol.anagramMappings(a, b),
            [1, 4, 3, 2, 0]
        )


if __name__ == '__main__':
    unittest.TestCase()

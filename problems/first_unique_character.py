# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string
import unittest


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1

        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1


class TestFirstUniqueChar(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.firstUniqChar('leetcode'), 0)
        self.assertEqual(sol.firstUniqChar('loveleetcode'), 2)


if __name__ == '__main__':
    unittest.TestCase()

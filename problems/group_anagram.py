# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams
import unittest


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            sorted_str = tuple(sorted(str))
            if sorted_str not in dic:
                dic[sorted_str] = [str]
            else:
                dic[sorted_str].append(str)
        return list(dic.values())


class TestGroupAnagram(unittest.TestCase):
    def test(self):
        sol = Solution()
        is_valid = True
        result = sol.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        true_set = [
            ['ate', 'eat', 'tea'],
            ['nat', 'tan'],
            ['bat']
        ]
        for s in result:
            s = sorted(s)
            if s not in true_set:
                is_valid = False
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.TestCase()

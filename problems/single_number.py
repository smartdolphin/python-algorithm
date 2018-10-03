# 136. Single Number
# https://leetcode.com/problems/single-number
import unittest


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                del dic[n]
        ret = None
        for k in dic.keys():
            ret = k
        return ret


class TestSingleNum(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.singleNumber([2, 2, 1]),
            1
        )
        self.assertEqual(
            sol.singleNumber([4,1,2,1,2]),
            4
        )


if __name__ == '__main__':
    unittest.TestCase()

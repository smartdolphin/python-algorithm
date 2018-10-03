#
#
import unittest


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                del dic[n]

        ret = []
        for n in dic.keys():
            ret.append(n)
        return ret


class TestSingleNumberIII(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.singleNumber([1, 2, 1, 3, 2, 5]),
            [3, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()

# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate
import unittest


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) <= 1:
            return False
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                return True
        return False


class TestContainDuplicate(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(sol.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(sol.containsDuplicate([1, 2, 3, 4]))
        self.assertTrue(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == '__main__':
    unittest.TestCase()

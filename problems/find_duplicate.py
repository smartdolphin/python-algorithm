# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array
import unittest


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        result = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                result.append(index + 1)
            else:
                nums[index] *= -1
        return result


class TestFindDuplicate(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]),
            [2, 3]
        )


if __name__ == '__main__':
    unittest.TestCase()

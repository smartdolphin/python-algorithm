# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position
import unittest


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        find = -1
        for i in range(len(nums)):
            if target <= nums[i]:
                find = i
                break
        if find == -1:
            find = len(nums)
        return find


class TestSearchInsertPosition(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.searchInsert([1, 3, 5, 6], 5),
            2
        )
        self.assertEqual(
            sol.searchInsert([1, 3, 5, 6], 2),
            1
        )
        self.assertEqual(
            sol.searchInsert([1, 3, 5, 6], 7),
            4
        )
        self.assertEqual(
            sol.searchInsert([1, 3, 5, 6], 0),
            0
        )


if __name__ == '__main__':
    unittest.TestCase()
